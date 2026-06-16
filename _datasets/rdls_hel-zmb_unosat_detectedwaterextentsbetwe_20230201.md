---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb
dataset_id: rdls_hel-zmb_unosat_detectedwaterextentsbetwe_20230201
description: "UNOSAT code FL20230131ZMB This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Southern, Lusaka, and Central Provinces, Zambia between 26\
  \ to 30 January 2023. Within the cloud free analyzed areas of about 20,000 km\xB2\
  \ and based on Worldpop spatial demographic data and the maximum flood water extent,\
  \ about 80,000 people out of 800,000 are potentially exposed or living close to\
  \ maximum floodwaters areas. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population living close to or potentially exposed to maximum floodwater
      areas based on WorldPop spatial demographic data
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed and compared VIIRS satellite imagery from\
    \ January 26-30, 2023 to detect cumulative water extents across cloud-free areas\
    \ (~20,000 km\xB2) in three Zambian provinces. Detected flood water polygons were\
    \ intersected with WorldPop gridded population data to estimate approximately\
    \ 80,000 people potentially exposed to maximum floodwater areas out of a total\
    \ population of 800,000 in the study region."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-between-26-and-30-january-2023-in-southern-lusaka-and-central-provinces-zamb
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to floodwaters during January 2023
      flood event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 26 and 30 January 2023 in
    Southern, Lusaka, and Central Provinces, Zambia (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3476/FL20220131ZMB_gdb.zip
  format: Geodatabase
  id: resource_7490c2c7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220131ZMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 26 and 30 January 2023 in
    Southern, Lusaka, and Central Provinces, Zambia (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3476/FL20230131ZMB_SHP.zip
  format: null
  id: resource_eb6601d3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230131ZMB_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 26 and 30 January 2023 in
    Southern, Lusaka, and Central Provinces, Zambia (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3476/Preliminary%20Satellite%20Derived%20Flood%20Evolution%20Assessment_FL20220131ZMB_Southern_Lusaka_Central_1Feb2023.csv
  format: null
  id: resource_f0202b74
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Preliminary Satellite Derived Flood Evolution Assessment_FL20220131ZMB_Southern_Lusaka_Central_1Feb2023.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-zmb_unosat_detectedwaterextentsbetwe_20230201
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-01'
temporal_resolution: null
title: Satellite detected water extents between 26 and 30 January 2023 in Southern,
  Lusaka, and Central Provinces, Zambia
version: null
vulnerability: null
---
