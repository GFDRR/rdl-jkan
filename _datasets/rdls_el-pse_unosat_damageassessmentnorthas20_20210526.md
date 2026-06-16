---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-north-gaza-as-of-20-may-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-north-gaza-as-of-20-may-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-north-gaza-as-of-20-may-2021
dataset_id: rdls_el-pse_unosat_damageassessmentnorthas20_20210526
description: 'UNOSAT code: CE20210515PSE This map illustrates a rapid satellite imagery
  based building damage analysis within an area of Gaza and North Gaza Governorates,
  Gaza Strip, Occupied Palestinian Territory based on an image collected on 20 May
  2021. According to satellite imagery analysis, there are visible 23 impact craters
  to roads, 331 destroyed or damaged buildings, and 131 areas of possible damage on
  the road or road-blocking debris. According to publicly available data about 12
  health care facilities and more than 40 educational facilities are located within
  100 meters of damaged areas and are shown on the map. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-north-gaza-as-of-20-may-2021]'
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
    description: Building stock in North Gaza assessed for damage from conflict-related
      impacts
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
    description: Road network and health/educational facilities assessed for damage
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
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted rapid satellite imagery analysis comparing
    pre- and post-event images collected on 20 May 2021 to identify visible damage
    signatures including destroyed/damaged buildings, impact craters, and road debris
    in North Gaza and Gaza Governorates. Results were compiled into geospatial vector
    datasets with damage classification attributes and confidence levels.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-north-gaza-as-of-20-may-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from satellite imagery showing
      331 destroyed or damaged buildings
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage including 23 impact craters to roads
      and road-blocking debris
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Palestine - Damage Assessment in North Gaza as of 20 May 2021 (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PS/CE20210515PSE/CE20210515PSE_gdb.zip
  format: Geodatabase
  id: resource_354321c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20210515PSE_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Damage Assessment in North Gaza as of 20 May 2021 (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/PS/CE20210515PSE/Damage_Site_20210520_6_attr.zip
  format: null
  id: resource_089ea534
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage_Site_20210520_6_attr.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_damageassessmentnorthas20_20210526
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-05-26'
temporal_resolution: null
title: Palestine - Damage Assessment in North Gaza as of 20 May 2021
version: null
vulnerability: null
---
