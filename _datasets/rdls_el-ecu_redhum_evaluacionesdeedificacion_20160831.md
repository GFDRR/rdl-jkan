---
attributions:
- entity:
    affiliation: null
    email: null
    name: MIDUVI (Ministerio de Desarrollo Urbano y Vivienda)
    url: https://data.humdata.org/dataset/evaluaciones-de-edificaciones-y-viviendas-miduvi-20160831
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Redhum (inactive)
  url: https://data.humdata.org/dataset/evaluaciones-de-edificaciones-y-viviendas-miduvi-20160831
creator:
  affiliation: null
  email: null
  name: Redhum (inactive)
  url: https://data.humdata.org/dataset/evaluaciones-de-edificaciones-y-viviendas-miduvi-20160831
dataset_id: rdls_el-ecu_redhum_evaluacionesdeedificacion_20160831
description: 'Evaluaciones de edificaciones y viviendas hasta el 31 de agosto.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/evaluaciones-de-edificaciones-y-viviendas-miduvi-20160831]'
details: null
exposure:
- asset_type:
    description: Building and housing stock assessed for structural condition and
      damage
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Building and housing damage assessments conducted by MIDUVI following
    the April 2016 Ecuador earthquake, compiled through field evaluations and aggregated
    as of 31 August 2016 to document direct structural impacts on the building stock.
  sources:
  - id: source_1
    license: null
    name: MIDUVI (Ministerio de Desarrollo Urbano y Vivienda)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/evaluaciones-de-edificaciones-y-viviendas-miduvi-20160831
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Post-event building and housing damage assessments from earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Ecuador - Evaluaciones de edificaciones y viviendas_MIDUVI 20160831
    (Evaluaciones de edificaciones y viviendas por MIDUVI fecha de corte 31-08-2016)
  download_url: https://data.humdata.org/dataset/d0f8719a-427a-4027-abfb-7a99b48eaaf2/resource/d2ecf4e5-a1f7-41ab-86dd-c95bd3a3bf9f/download/miduvi_evaluacionedificaciones_20160831.xls
  format: null
  id: resource_d2ecf4e5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MIDUVI_EVALUACIONEDIFICACIONES_20160831.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ecu_redhum_evaluacionesdeedificacion_20160831
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-31'
temporal_resolution: null
title: Ecuador - Evaluaciones de edificaciones y viviendas_MIDUVI 20160831
version: null
vulnerability: null
---
