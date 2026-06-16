---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province
dataset_id: rdls_hel-tha_unosat_detectedwaterextents1augu_20241016
description: "UNOSAT code: FL20240912THA This map illustrates cumulative detected\
  \ water using multiple satellites and drone in Phayao Province, Thailand from 1\
  \ August to 12 October 2024. Within the analysed area of about 6,200 km\xB2, a total\
  \ of about 360 km\xB2 of land appears to be affected by flood waters, with around\
  \ 330 km\xB2 of cropland inundated. Based on Worldpop spatial demographic data,\
  \ about 13,500 people are exposed or living close to flooded areas from 1 August\
  \ to 12 October 2024. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province]"
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
    description: "Cropland inundated by flood waters, approximately 330 km\xB2 affected"
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population exposed or living close to flooded areas based on WorldPop
      spatial demographic data
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
  event_sets:
  - analysis_type: probabilistic
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
  description: "UNOSAT analysts processed multi-satellite and drone imagery from 1\
    \ August to 12 October 2024, comparing temporal image pairs to detect notable\
    \ changes and delineate water extents. Detected water polygons were intersected\
    \ with WorldPop population grids and agricultural land use data to estimate exposure\
    \ and direct impacts. The analysis covers approximately 6,200 km\xB2 in Phayao\
    \ Province, Thailand."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-from-1-august-2024-to-12-october-2024-over-phayao-province
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: "Direct cropland inundation from flood event, approximately 330 km\xB2\
      \ of agricultural land affected"
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposed or living close to flooded areas, approximately
      13,500 people affected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Thailand - Satellite detected water extents from 1 August 2024 to 12
    October 2024 over Phayao Province (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4003/FL20240912THA_GDB.zip
  format: Geodatabase
  id: resource_cd4e3993
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912THA_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Thailand - Satellite detected water extents from 1 August 2024 to 12
    October 2024 over Phayao Province (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4003/FL20240912THA_SHP.zip
  format: null
  id: resource_7efe4382
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912THA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-tha_unosat_detectedwaterextents1augu_20241016
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-16'
temporal_resolution: null
title: Thailand - Satellite detected water extents from 1 August 2024 to 12 October
  2024 over Phayao Province
version: null
vulnerability: null
---
