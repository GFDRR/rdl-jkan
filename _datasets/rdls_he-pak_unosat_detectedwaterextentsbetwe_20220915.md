---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan
dataset_id: rdls_he-pak_unosat_detectedwaterextentsbetwe_20220915
description: "UNOSAT code FL20220808PAK, GDACS Id: 1101522 This map illustrates cumulative\
  \ satellite-detected water using VIIRS in Pakistan between 01 to 07 September 2022.\
  \ Within the analyzed area of about 880,000 km\xB2, a total of about 60,000 km\xB2\
  \ of lands appear to be affected with flood waters. Floodwaters seem to have decreased\
  \ of about 25,000 km\xB2 since the period between the 01st July to 31rd of August\
  \ 2022. Based on Worldpop population data and the maximum flood water coverage,\
  \ at least 22 million people were potentially exposed or living close to flooded\
  \ areas in August 2022. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Dotted line represents approximately the Line of Control in Jammu and\
  \ Kashmir agreed upon by India and Pakistan. The final status of Jammu and Kashmir\
  \ has not been agreed upon by the parties. The boundaries and names shown, and the\
  \ designations used on this map do not imply official endorsement or acceptance\
  \ by the United Nations. The United Nations Satellite Centre - UNOSAT is not responsible\
  \ for the misuse or misrepresentation of the map.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan]"
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 1-7 September\
    \ 2022, comparing multi-temporal observations to detect cumulative water extents\
    \ across Pakistan. Detected inundation areas (approximately 60,000 km\xB2) were\
    \ intersected with WorldPop population data to estimate approximately 22 million\
    \ people potentially exposed to flooded areas."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan
  rel: source
loss: null
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
  description: Satellite detected water extents between 01 and 07 September 2022 over
    Pakistan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3372/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_56afd1fa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 01 and 07 September 2022 over
    Pakistan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3372/FL20220808PAK_SHP.zip
  format: null
  id: resource_e0b7a955
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 01 and 07 September 2022 over
    Pakistan (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3372/UNOSAT_Population_Exposure_FL20220808PAK_20220825_20220831_20220901_20220907_Updated14Sep2022.xlsx
  format: null
  id: resource_c28e62cc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20220808PAK_20220825_20220831_20220901_20220907_Updated14Sep2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextentsbetwe_20220915
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
  start: '2022-09-15'
temporal_resolution: null
title: Satellite detected water extents between 01 and 07 September 2022 over Pakistan
version: null
vulnerability: null
---
