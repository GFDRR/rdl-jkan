---
attributions:
- entity:
    affiliation: null
    email: null
    name: SISMICEDE CONRED Guatemala
    url: https://data.humdata.org/dataset/incidentes
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentes
creator:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentes
dataset_id: rdls_el-gtm_conred_desastresnaturalesinciden_2012
description: "Incidentes atendidos por la CONRED en el a\xF1o 2012, en todo el territorio\
  \ de Guatemala, con estad\xEDsticas de personas y viviendas, el tipo de evento y\
  \ la clasificaci\xF3n de la CONRED, Departamento y Municipio y en algunos centros\
  \ poblados.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/incidentes]"
details: null
exposure:
- asset_type:
    description: Housing units (viviendas) affected by natural disaster incidents
      in Guatemala during 2012
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
    description: Persons affected by natural disaster incidents in Guatemala during
      2012
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event incident data collected and registered by CONRED through
    SISMICEDE system during 2012 across all Guatemalan territory, documenting natural
    disaster events by type, geographic location (department and municipality), and
    impacts on population and housing stock.
  sources:
  - id: source_1
    license: null
    name: SISMICEDE CONRED Guatemala
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/incidentes
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood incidents recorded by CONRED in 2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  - asset_category: buildings
    asset_dimension: structure
    description: Housing units affected by flood incidents recorded by CONRED in 2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide incidents recorded by CONRED in
      2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
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
  - asset_category: buildings
    asset_dimension: structure
    description: Housing units affected by landslide incidents recorded by CONRED
      in 2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes A\xF1o 2012 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2012)"
  download_url: https://data.humdata.org/dataset/5ff71b2d-9c34-4c9e-babb-4802ae0ad26f/resource/91153e67-3c28-4b42-a06c-293e23cedb54/download/incidentes-2012.xls
  format: null
  id: resource_91153e67
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Incidentes 2012.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-gtm_conred_desastresnaturalesinciden_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2012-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: "Guatemala - Desastres Naturales - Incidentes A\xF1o 2012"
version: null
vulnerability: null
---
