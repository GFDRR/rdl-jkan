---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria
dataset_id: rdls_hel-nga_unosat_detectedwaterextents913no_20241115
description: "UNOSAT code: FL20240902NGA, GDACS ID: 1102720 This map illustrates cumulative\
  \ satellite-detected water using VIIRS in Nigeria between 09 to 13 November 2024.\
  \ Within the cloud free analysed areas of about 900,000 km\xB2, a total of about\
  \ 22,000 km\xB2 of lands appear to be affected with flood waters. Maximum flood\
  \ water extent appears to have receded of about 5,700 km\xB2 since the period between\
  \ 27 to 31 October 2024. Based on Worldpop population data and the maximum flood\
  \ water extent, about 5.8 million people remain potentially exposed or live close\
  \ to flooded areas. The pixelwise water fraction from VIIRS, using a 5-day composite\
  \ at 375 m spatial resolution, indicates potential floodwater coverage ranging from\
  \ 0% to 100%. This large-scale analysis is intended for guidance purposes and has\
  \ not yet been validated with ground truth data or higher- resolution analysis.\
  \ The population exposure analysis is based on floodwaters observed only in cloud-free\
  \ areas, so the total number of people exposed may be underestimated. This is a\
  \ preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria]"
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
    description: Population potentially exposed to or living close to flooded areas
      based on WorldPop data and maximum flood extent
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
  description: "UNOSAT analysts processed VIIRS satellite imagery from 9-13 November\
    \ 2024, comparing multi-temporal observations to detect water extent changes and\
    \ identify flood-affected areas. WorldPop population data was overlaid with maximum\
    \ flood extent to estimate population exposure. The dataset provides cumulative\
    \ water detection across approximately 900,000 km\xB2 of cloud-free analysis area."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-from-9-to-13-november-2024-over-nigeria
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood waters detected via satellite imagery
      during November 2024
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected water extents from 9 to 13 November 2024 over Nigeria
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4021/FL20240902NGA_gdb.zip
  format: Geodatabase
  id: resource_3930e5f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from 9 to 13 November 2024 over Nigeria
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4021/FL20240902NGA_SHP.zip
  format: null
  id: resource_8791c413
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from 9 to 13 November 2024 over Nigeria
    (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4021/UNOSAT_Population_Exposure_FL20240902NGA_27_30_October_09_13_November_Nigeria.xlsx
  format: null
  id: resource_c4d30e3b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240902NGA_27_30_October_09_13_November_Nigeria.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nga_unosat_detectedwaterextents913no_20241115
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
  start: '2024-11-15'
temporal_resolution: null
title: Satellite detected water extents from 9 to 13 November 2024 over Nigeria
version: null
vulnerability: null
---
