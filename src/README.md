# GE walkthrough

## How to work with Great Expectations

1. Let Great Expectations create a simple first draft suite, by running `great_expectations suite new`.
2. View the suite here in Data Docs.
3. Edit the suite in a Jupyter notebook by running `great_expectations suite edit`
4. Repeat Steps 2-3 until you are happy with your suite.
5. Commit this suite to your source control repository.

## What are Expectations?

```text
expect_column_to_exist
expect_table_row_count_to_be_between
expect_column_values_to_be_unique
expect_column_values_to_not_be_null
expect_column_values_to_be_between
expect_column_values_to_match_regex
expect_column_mean_to_be_between
expect_column_kl_divergence_to_be_less_than
... and many more
```

An expectation is a falsifiable, verifiable statement about data.
Expectations provide a language to talk about data characteristics and data quality - humans to humans, humans to machines and machines to machines.

Expectations are both data tests and docs!

## Expectations can be presented in a machine-friendly JSON

```json
{
    "expectation_type": "expect_column_values_to_not_be_null",
    "kwargs": {
        "column": "user_id"
    }
}
```

A machine can test if a dataset conforms to the expectation.

## Validation produces a validation result object

```json
{
    "success": false,
    "result": {
        "element_count": 253405,
        "unexpected_count": 7602,
        "unexpected_percent": 2.999
    },
    "expectation_config": {
        "expectation_type": "expect_column_values_to_not_be_null",
        "kwargs": {
            "column": "user_id"
        }
}
```

Here's an example Validation Result (not from your data) in JSON format. This object has rich context about the test failure.

## Validation results save you time

![validation_failed_unexpected_values.gif](../res/validation_failed_unexpected_values.gif)

This is an example of what a single failed Expectation looks like in Data Docs. Note the failure includes unexpected values from your data. This helps you debug pipelines faster.

## Great Expectations provides a large library of expectations

![glossary_scroller.gif](../res/glossary_scroller.gif)

[Nearly 50 built in expectations](https://greatexpectations.io/expectations) allow you to express how you understand your data, and you can add custom expectations if you need a new one.
