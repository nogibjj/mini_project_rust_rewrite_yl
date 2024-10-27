use individual_project_2_yl::{extract, query, transform_load};

#[test]
fn test_extract() {
    let url =
        "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/candy-power-ranking/candy-data.csv";
    let file_path = "data/candy-data.csv";
    let directory = "data";

    extract(url, file_path, directory);

    assert!(std::fs::metadata(file_path).is_ok());
}

#[test]
fn test_transform_load() {
    let dataset = "data/candy-data.csv";
    let result = transform_load(dataset);

    assert_eq!(result.unwrap(), "candy_data_DB.db");
}

#[test]
fn test_query() {
    // Execute a SELECT query
    let select_query = "SELECT * FROM candy_data_DB WHERE competitorname = '100 Grand';";
    let result = query(select_query);

    assert!(result.is_ok());
}
