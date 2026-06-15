---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria
dataset_id: rdls_he-nga_unosat_detectedwaterextentsbetwe_20221027
description: "UNOSAT code FL20221019NGA This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Nigeria between 1 to 25 October 2022 compared with the period\
  \ from 1 to 30 September 2022. Within the cloud free analysed areas of about 912,000\
  \ km\xB2, a total of about 48,300 km\xB2 of land appears to be affected. In the\
  \ analysed areas, 1,370 health facilities and 2,730 schools are identified to be\
  \ within or close to a flooded zone. In comparison with the period between 1 to\
  \ 30 September 2022, water extent appears to have increased of about 2,300 km\xB2\
  . Based on Worldpop population data and the maximal flood water extent ~12,200,000\
  \ people are potentially exposed or living close to flooded areas amongst the 220\
  \ million people living in the analysed zone. This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria]"
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
  description: "UNOSAT analysts compared VIIRS satellite imagery from 1-25 October\
    \ 2022 with baseline imagery from 1-30 September 2022 to detect cumulative water\
    \ extents across Nigeria. Cloud-free areas of 912,000 km\xB2 were analyzed to\
    \ identify 48,300 km\xB2 of inundated land. Infrastructure locations (health facilities,\
    \ schools) and population data from Worldpop were spatially intersected with detected\
    \ flood extents to quantify exposure and impacts."
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
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria
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
  description: Satellite detected water extents between 1 and 25 October 2022 over
    Nigeria (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3427/FL20221019NGA_GDB.zip
  format: Geodatabase
  id: resource_3d701d8c
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
  description: Satellite detected water extents between 1 and 25 October 2022 over
    Nigeria (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3427/FL20221019NGA_SHP.zip
  format: null
  id: resource_f6e4a5e1
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
  description: Satellite detected water extents between 1 and 25 October 2022 over
    Nigeria (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3427/Satellite%20detected%20water%20extents%20between%20September%202022%20and%20October%202022%20over%20Nigeria.csv
  format: null
  id: resource_b2fb532a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents between September 2022 and October 2022
    over Nigeria.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-nga_unosat_detectedwaterextentsbetwe_20221027
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
  start: '2022-10-27'
temporal_resolution: null
title: Satellite detected water extents between 1 and 25 October 2022 over Nigeria
version: null
vulnerability: null
---
