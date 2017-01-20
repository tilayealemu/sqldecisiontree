from __future__ import print_function

import sys

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

TARGET = "TARGET_FIELD"


def get_data(filepath):
    return pd.read_csv(filepath, index_col=0)


def encode_col(df, col_name):
    target_values = df[col_name].unique()
    target_to_int = {target_value: encoding for encoding, target_value in enumerate(target_values)}
    df2 = df.copy()
    df2[TARGET] = df2[col_name].replace(target_to_int)
    return df2, target_values


def fit_dt(df, features):
    y = df[TARGET]
    X = df[features]
    dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
    dt.fit(X, y)
    return dt


def to_sql(tree, features, targets):
    t = tree.tree_
    return to_sql_recurse(t.children_left, t.children_right, t.threshold, features, targets, tree.tree_.value, 0, 0)


def to_sql_recurse(left, right, conditions, features, targets, leaves, node_pos, depth):
    sql = ""
    if conditions[node_pos] == -2:
        selected_feature = targets[np.argmax(leaves[node_pos])]
        sql += indent(depth) + "'" + selected_feature + "'"
    else:
        sql += indent(depth) + "CASE WHEN " + features[node_pos] + " <= " + str(
            conditions[node_pos]) + " THEN "
        if left[node_pos] != -1:
            sql += to_sql_recurse(left, right, conditions, features, targets, leaves, left[node_pos],
                                  depth + 1)
        sql += indent(depth) + "ELSE"
        if right[node_pos] != -1:
            sql += to_sql_recurse(left, right, conditions, features, targets, leaves, right[node_pos],
                                  depth + 1)
        sql += indent(depth) + "END"
    return sql


def indent(depth):
    return "\n" + " " * 2 * depth


filepath = sys.argv[1]
df = get_data(filepath)
df2, targets = encode_col(df, "Name")
features = list(df2.columns[:3])
dt = fit_dt(df2, features)
sql = to_sql(dt, [features[i] for i in dt.tree_.feature], targets)
print(sql)
