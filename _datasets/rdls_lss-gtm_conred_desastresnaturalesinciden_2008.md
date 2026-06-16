---
attributions:
- entity:
    affiliation: null
    email: null
    name: CONRED Guatemala
    url: https://data.humdata.org/dataset/incidentes-2008-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentes-2008-2017
creator:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentes-2008-2017
dataset_id: rdls_lss-gtm_conred_desastresnaturalesinciden_2008
description: "Incidentes atendidos por la CONRED del a\xF1o 2008 al a\xF1o 2017 ,\
  \ en todo el territorio de Guatemala, con estad\xEDsticas de personas y viviendas,\
  \ tipo de evento segun la clasificaci\xF3n de la CONRED, Departamento, Municipio\
  \ y centros poblados.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/incidentes-2008-2017]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "CONRED (Coordinadora Nacional para la Reducci\xF3n de Desastres) compiled\
    \ incident records from emergency response operations across Guatemala from 2008-2017,\
    \ documenting natural disaster events by type, location (department/municipality),\
    \ and direct impacts (persons affected, dwellings damaged). Data were organized\
    \ by year in separate spreadsheets and classified according to CONRED's hazard\
    \ taxonomy."
  sources:
  - id: source_1
    license: null
    name: CONRED Guatemala
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/incidentes-2008-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide events
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from strong wind events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_5
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
    description: Population affected by strong wind events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_6
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Excel)"
  download_url: https://drive.google.com/file/d/1n9P2y0EXHBwt8qn8fCQAd1eReDkfTcqd/view?usp=drive_web
  format: null
  id: resource_d45e4585
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2017.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2008)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/11aa7d57-e840-4e59-af3a-931b254001be/download/incidentes-2008.xlsx
  format: null
  id: resource_11aa7d57
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2008.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2009)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/1c0a770b-83d5-4749-9cc0-9ecb10ce0cc8/download/incidentes-2009.xlsx
  format: null
  id: resource_1c0a770b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2009.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2010)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/da50e8e0-2ced-4c4e-93cd-964e883b863e/download/incidentes-2010.xlsx
  format: null
  id: resource_da50e8e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2010.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2011)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/b18e7deb-1dca-442f-baf1-4d0629475492/download/incidentes-2011.xlsx
  format: null
  id: resource_b18e7deb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2011.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2013)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/0743526b-fd3a-4913-8ed0-163cb76fc5ea/download/incidentes-2013.xlsx
  format: null
  id: resource_0743526b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2013.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2014)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/b65f8d23-c31f-4264-ad5a-6350f38e6397/download/incidentes-2014.xlsx
  format: null
  id: resource_b65f8d23
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2014.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2015)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/b0d7442e-bffe-4f53-98bf-f2bf0b9b2db1/download/incidentes-2015.xlsx
  format: null
  id: resource_b0d7442e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2015.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017 (Incidentes\
    \ atendidos por la CONRED Guatemala en el a\xF1o 2016)"
  download_url: https://data.humdata.org/dataset/39ecc6ca-f1a7-4df3-8b2e-3f7f44d6b7ae/resource/dc6431b4-07e9-466d-9873-20aa9a0a7550/download/incidentes-2016.xlsx
  format: null
  id: resource_dc6431b4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INCIDENTES 2016.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_conred_desastresnaturalesinciden_2008
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
  end: '2017-06-30'
  start: '2008-01-01'
temporal_resolution: null
title: "Guatemala - Desastres Naturales - Incidentes a\xF1os 2008 - 2017"
version: null
vulnerability: null
---
