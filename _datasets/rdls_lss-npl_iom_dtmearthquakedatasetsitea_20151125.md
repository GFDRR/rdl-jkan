---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Nepal
    url: https://data.humdata.org/dataset/io
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/io
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/io
dataset_id: rdls_lss-npl_iom_dtmearthquakedatasetsitea_20151125
description: 'This data is about a preliminary assessment to displacement sites in
  Nepal 2015. This dataset contains rounds 1 through 5.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/io]'
details: Preliminary Assessment. Data is frequently updated. Please refer to the description
  of the datasets to identify the latest information.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM conducted direct observational assessments of displacement sites
    across Nepal following the 2015 earthquake, collecting data through 5 rounds of
    the Displacement Tracking Matrix (DTM). Site-level data on displaced populations
    and camp management conditions were compiled into standardized CCCM and DTM formats
    for humanitarian response coordination.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Nepal
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/io
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement of populations from earthquake-affected sites in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - IOM DTM Earthquake Dataset - Site assessment data (Data updated
    as of November 25, 2015)
  download_url: https://data.humdata.org/dataset/2c626380-4c70-4396-b467-36d8916960cf/resource/457477e4-164f-4d7c-b55c-38799765a518/download/cccm-nepal-dtm.xlsx
  format: null
  id: resource_457477e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CCCM Nepal - DTM.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - IOM DTM Earthquake Dataset - Site assessment data (CSV contained
    merged DTM data from all rounds.)
  download_url: https://data.humdata.org/dataset/2c626380-4c70-4396-b467-36d8916960cf/resource/f6bbbc39-cdd5-4d32-a058-58088af67106/download/cccm-nepal-displacement-tracking-matrix.csv
  format: null
  id: resource_f6bbbc39
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cccm-nepal-displacement-tracking-matrix.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_iom_dtmearthquakedatasetsitea_20151125
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-25'
temporal_resolution: null
title: Nepal - IOM DTM Earthquake Dataset - Site assessment data
version: null
vulnerability: null
---
