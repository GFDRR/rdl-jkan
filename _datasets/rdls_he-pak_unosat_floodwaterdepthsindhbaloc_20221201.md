---
attributions:
- entity:
    affiliation: null
    email: null
    name: Suomi-NPP & NOAA-20 VIIRS satellite imagery
    url: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022
dataset_id: rdls_he-pak_unosat_floodwaterdepthsindhbaloc_20221201
description: 'UNOSAT code FL20221121PAK This map illustrates floodwater depth in Sindh
  and Balochistan Provinces, Pakistan using water flood depth deduced from Suomi-NPP
  & NOAA-20 VIIRS as of 29 November 2022. Within the cloud free analyzed areas of
  about 40,000 km2, a total of about 47,000 km2 of lands appear to be affected with
  flood waters.Based on Worldpop population data and the maximum flood water coverage,
  ~2 million people are potentially exposed or living close to flooded areas. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022]'
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
    description: Population potentially exposed to floodwaters based on WorldPop data
      and maximum flood coverage
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Suomi-NPP and NOAA-20 VIIRS satellite imagery
    acquired on 29 November 2022, comparing cloud-free areas to detect floodwater
    extent and derive depth estimates. Population exposure was calculated by intersecting
    the maximum flood coverage with WorldPop gridded population data to estimate approximately
    2 million people potentially affected in Sindh and Balochistan Provinces.
  sources:
  - id: source_1
    license: null
    name: Suomi-NPP & NOAA-20 VIIRS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/floodwater-depth-in-sindh-and-balochistan-provinces-pakistan-as-of-29-november-2022
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
  description: Floodwater depth in Sindh and Balochistan Provinces, Pakistan as of
    29 November 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3457/FL20221121PAK.gdb.zip
  format: Geodatabase
  id: resource_984301b0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221121PAK.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floodwater depth in Sindh and Balochistan Provinces, Pakistan as of
    29 November 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3457/FL20221121PAK_SHP.zip
  format: null
  id: resource_3434f994
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221121PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floodwater depth in Sindh and Balochistan Provinces, Pakistan as of
    29 November 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3457/Preliminary%20Satellite%20Derived%20Flood%20Evolution%20Assessment%2C%20Islamic%20Republic%20of%20Pakistan.csv
  format: null
  id: resource_f574ade2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_floodwaterdepthsindhbaloc_20221201
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-12-01'
temporal_resolution: null
title: Floodwater depth in Sindh and Balochistan Provinces, Pakistan as of 29 November
  2022
version: null
vulnerability: null
---
