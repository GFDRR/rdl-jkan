---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan
dataset_id: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20240816
description: "UNOSAT code: FL20240425SSD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in South Sudan between 10 to 14 August 2024 compared with the\
  \ period from 01 to 05 August 2024. Within the cloud free analysed areas of about\
  \ 620,000 km\xB2, a total of about 30,000 km\xB2 of lands appear to be affected\
  \ with flood waters. Water extent appears to have increased of about 1,800 km\xB2\
  \ since the period between 01 to 05 August 2024. Based on Worldpop population data\
  \ and the maximal flood water extent ~505,000 people are potentially exposed or\
  \ living close to flooded areas. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan]"
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: VIIRS satellite imagery from 10-14 August 2024 was analyzed and compared
    with imagery from 01-05 August 2024 to detect cumulative water extents. Analysts
    reviewed satellite imagery to identify notable changes between time periods. Population
    exposure was estimated by intersecting the maximal flood water extent with WorldPop
    gridded population data to quantify potentially affected populations.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan
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
  description: Satellite detected water extents between 10 and 14 August 2024 over
    South Sudan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3915/FL20220424SSD_gdb.zip
  format: Geodatabase
  id: resource_7854b770
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220424SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 10 and 14 August 2024 over
    South Sudan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3915/FL20220424SSD_SHP.zip
  format: null
  id: resource_f5a7043f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220424SSD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 10 and 14 August 2024 over
    South Sudan (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3915/UNOSAT_Population_Exposure_FL20220424SSD_10Aug_14Aug2024_SouthSudan_Week20.xlsx
  format: null
  id: resource_f03d6d88
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20220424SSD_10Aug_14Aug2024_SouthSudan_Week20.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20240816
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-16'
temporal_resolution: null
title: Satellite detected water extents between 10 and 14 August 2024 over South Sudan
version: null
vulnerability: null
---
