---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua
dataset_id: rdls_he-nic_unosat_detectedwaterextentsbetwe_20221018
description: "UNOSAT code TC20221014NIC This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Nicaragua between 12 to 16 October 2022 compared with the\
  \ period from 27 September to 01 October 2022. Within the cloud free analyzed areas\
  \ of about 240,000 km\xB2, a total of about 3,200 km\xB2 of lands appear to be affected.\
  \ Water extent appears to have increased of about 2,300 km\xB2 since the period\
  \ between 27 September to 01 October 2022. Based on Worldpop population data and\
  \ the maximal flood water extent ~120,000 people are potentially exposed or living\
  \ close to flooded areas amongst the 6,570,000 people living in cloud free areas.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua]"
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
      estimated at approximately 120,000 people based on WorldPop data
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery acquired between
    12-16 October 2022, comparing water extent with baseline imagery from 27 September
    to 1 October 2022 to detect cumulative flood inundation. Detected water extents
    were vectorized and integrated with WorldPop population data to estimate population
    exposure to the observed flood hazard during the tropical cyclone event.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-12-and-16-october-2022-over-nicaragua
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
  description: Satellite detected water extents between 12 and 16 October 2022 over
    Nicaragua (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3410/TC20221014NIC_gdb.zip
  format: Geodatabase
  id: resource_5fe3bb05
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221014NIC_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 12 and 16 October 2022 over
    Nicaragua (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3410/TC20221014NIC_SHP.zip
  format: null
  id: resource_d7492ec6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221014NIC_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 12 and 16 October 2022 over
    Nicaragua (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3410/UNOSAT_Population_Exposure_TC20221014NIC_Nicaragua_16Oct2022.xlsx
  format: null
  id: resource_25095ba1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20221014NIC_Nicaragua_16Oct2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-nic_unosat_detectedwaterextentsbetwe_20221018
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-18'
temporal_resolution: null
title: Satellite detected water extents between 12 and 16 October 2022 over Nicaragua
version: null
vulnerability: null
---
