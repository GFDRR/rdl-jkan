---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad
dataset_id: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20240905
description: "UNOSAT code: FL20240820TCD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Chad between 31 August to 04 September 2024. Within the cloud\
  \ free analysed areas of about 900,000 km\xB2, a total of about 22,800 km\xB2 of\
  \ lands appear to be affected with flood waters. Maximum flood water extent appears\
  \ to have increased of about 3,900 km\xB2 since the period between 20 to 24 August\
  \ 2024. Based on Worldpop population data and the maximum flood water extent, about\
  \ 820,000 people are potentially exposed or living close to flooded areas. Amongst\
  \ which ~145,000 people in Logone Oriental Region and ~90,000 people in Mayo-Kebbi\
  \ Est Region. This is a preliminary analysis and has not yet been validated in the\
  \ field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad]"
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
    description: Population potentially exposed or living close to flooded areas,
      estimated at approximately 820,000 people based on WorldPop data
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery acquired between
    31 August and 04 September 2024, comparing multi-temporal images to detect water
    extent changes and map cumulative inundation. Detected water polygons were integrated
    with WorldPop gridded population data to estimate population exposure to flooded
    areas, producing vector geodatabase and shapefile outputs with confidence and
    validation fields.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad
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
  description: Satellite detected water extents between 31 August and 04 September
    2024 over Chad (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3949/FL20240820TCD_gdb.zip
  format: Geodatabase
  id: resource_452b5165
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 31 August and 04 September
    2024 over Chad (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3949/FL20240820TCD_SHP.zip
  format: null
  id: resource_0ada59e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 31 August and 04 September
    2024 over Chad (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3949/UNOSAT_Population_Exposure_FL20240820TCD_31Aug_04Sep2024_Chad.xlsx
  format: null
  id: resource_1f1c8b63
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240820TCD_31Aug_04Sep2024_Chad.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20240905
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-05'
temporal_resolution: null
title: Satellite detected water extents between 31 August and 04 September 2024 over
  Chad
version: null
vulnerability: null
---
