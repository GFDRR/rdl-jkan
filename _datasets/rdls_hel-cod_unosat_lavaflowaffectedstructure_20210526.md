---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no
dataset_id: rdls_hel-cod_unosat_lavaflowaffectedstructure_20210526
description: 'UNOSAT code: VO20210523COD This map illustrates potentially affected
  structures and buildings north of Goma airport, Nord-Kivu province, D.R. of the
  Congo as detected by satellite image acquired after the eruption of the Mount Nyiragongo
  euption of 22 May 2021. UNITAR-UNOSAT analysis used a Sentinel-1 image acquired
  on 25 May 2021, at 16:21 UTC, to extract the lava flow extent. Within this map extent,
  1,540 structures and 9 km of roads appear to be affected by the lava. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no]'
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
    description: Building structures north of Goma airport affected by lava flow
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network segments affected by lava flow
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: h_vaf:mm
      process: lava
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1 satellite imagery acquired on
    25 May 2021 to delineate lava flow extent from the Mount Nyiragongo eruption.
    Affected structures and road segments were identified through satellite image
    interpretation and spatial overlay analysis. This preliminary post-event damage
    assessment has not been validated in the field.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to 1,540 structures from lava flow inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to 9 km of roads from lava flow inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Lava flow and affected structures caused by the volcanic eruption of
    the 22 May 2021 in north of Goma airport, DR Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_gdb.zip
  format: Geodatabase
  id: resource_d81ed3f3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Lava flow and affected structures caused by the volcanic eruption of
    the 22 May 2021 in north of Goma airport, DR Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_SHP.zip
  format: null
  id: resource_d609f3f7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_unosat_lavaflowaffectedstructure_20210526
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-05-26'
temporal_resolution: null
title: Lava flow and affected structures caused by the volcanic eruption of the 22
  May 2021 in north of Goma airport, DR Congo
version: null
vulnerability: null
---
