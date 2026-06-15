---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria
dataset_id: rdls_he-nga_unosat_detectedwaterextentsbetwe_20221025
description: "UNOSAT code FL20221019NGA This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Nigeria between 19 to 23 October 2022 compared with the period\
  \ from 13 to 17 October 2022. Within the cloud free analysed areas of about 873,000\
  \ km\xB2, a total of about 25,000 km\xB2 of land appears to be affected. In the\
  \ analysed areas, 664 health facilities and 1,160 schools are identified to be within\
  \ or close to a flooded zone. In comparison with the period between 13 to 17 October\
  \ 2022, water extent appears to have decreased of about 5,000 km\xB2. Based on Worldpop\
  \ population data and the maximal flood water extent ~5,200,000 people are potentially\
  \ exposed or living close to flooded areas amongst the 197 million people living\
  \ in the analysed zone. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria]"
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
    description: Health facilities and schools identified within or close to flooded
      zones
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population exposed to flooding based on WorldPop gridded population
      data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
    19-23 October 2022, comparing multi-temporal scenes to detect water extent changes
    relative to a baseline period (13-17 October 2022). Water extent polygons were
    delineated through visual interpretation and automated change detection. Exposure
    analysis overlaid detected flood areas with WorldPop population grids and facility
    registries to quantify affected populations and critical infrastructure.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-19-and-23-october-2022-over-nigeria
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
  description: Satellite detected water extents between 19 and 23 October 2022 over
    Nigeria (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3424/FL20221019NGA_GDB.zip
  format: Geodatabase
  id: resource_737f3e65
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019NGA_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 19 and 23 October 2022 over
    Nigeria (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3424/FL20221019NGA_SHP.zip
  format: null
  id: resource_8f7efc0e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019NGA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 19 and 23 October 2022 over
    Nigeria (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3424/Satellite%20detected%20water%20extents%20between%2019%20and%2023%20October%202022%20over%20Nigeria.csv
  format: null
  id: resource_49ed2985
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents between 19 and 23 October 2022 over Nigeria.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-nga_unosat_detectedwaterextentsbetwe_20221025
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-25'
temporal_resolution: null
title: Satellite detected water extents between 19 and 23 October 2022 over Nigeria
version: null
vulnerability: null
---
