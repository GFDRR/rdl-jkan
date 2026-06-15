---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/lake-chad-basin-baseline-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lake-chad-basin-baseline-population
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lake-chad-basin-baseline-population
dataset_id: rdls_exp-cmrnerngatcd_ocharowca_lakebasinbaselinepopulati_20160319
description: 'The data contains the latest estimated population of each administrative
  level 1 unit in the Lake Chad Basin. Estimation is based on input from UNFPA and
  the most recently available census for each country. Data is encoded as utf-8. The
  second row of the CSV contains HXL tags.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/lake-chad-basin-baseline-population]'
details: Estimates may not be endorsed by the national statistical offices but projections
  are based on data produced by United Nations entities and affiliates with mandate
  for data collection, compilation and dissemination.
exposure:
- asset_type:
    description: Estimated population by administrative level 1 units in the Lake
      Chad Basin
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Population estimates were derived by integrating UNFPA data with the
    most recently available national census data for each country in the Lake Chad
    Basin, aggregated to administrative level 1 units to establish baseline population
    distribution across the region.
  sources:
  - id: source_1
    license: null
    name: UNFPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lake-chad-basin-baseline-population
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Field Definitions -- Country, #country+name: Country in which the
    population is located -- ReportedLocation, #adm1+name: Administrative Unit Level
    1 in which the population is located -- TotalTotal, #population: total estimated
    population -- AsOfDate, #date: date for which the population estimate is made'
  download_url: https://data.humdata.org/dataset/75ed82f7-b03d-47e4-ba9b-c746412effe9/resource/020000e5-e7aa-4027-b58a-efe7396ff32e/download/lake_chad_basin_estimated_population_2017-02-23.csv
  format: null
  id: resource_020000e5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Lake_Chad_Basin_Estimated_Population_2017-02-23.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cmrnerngatcd_ocharowca_lakebasinbaselinepopulati_20160319
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  - CMR
  - NER
  - NGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-19'
temporal_resolution: null
title: Lake Chad Basin Baseline Population
version: null
vulnerability: null
---
