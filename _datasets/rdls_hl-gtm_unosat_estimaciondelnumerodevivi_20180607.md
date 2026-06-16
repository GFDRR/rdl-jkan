---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus EMS
    url: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-
dataset_id: rdls_hl-gtm_unosat_estimaciondelnumerodevivi_20180607
description: "Este mapa ilustra una estimaci\xF3n del n\xFAmero de viviendas y estructuras\
  \ potencialmente afectadas por el flujo pirocl\xE1stico detectado por Copernicus\
  \ EMS, usando una imagen sat\xE9lite Sentinel-2 colectada el 4 de junio 2018. UNITAR-UNOSAT\
  \ ha estimado un total de 411 viviendas / estructuras que se encuentran dentro del\
  \ \xE1rea afectada por el flujo pirocl\xE1stico; de las cuales 260 pertenecen a\
  \ la aldea de San Miguel de Los Lotes. Complejos industriales y hoteleros como el\
  \ de La Reuni\xF3n se encuentran tambi\xE9n dentro de la extensi\xF3n del flujo\
  \ pirocl\xE1stico. Este an\xE1lisis es preliminar y no ha sido validado en terreno.\
  \ Por favor, env\xEDen sus comentarios a UNITAR-UNOSAT.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets_by_hazard_type:
    volcanic:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: h_vaf:mm
        process: pyroclastic_flow
        trigger: null
        type: volcanic
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery collected on
    4 June 2018 and compared it with reference imagery to detect pyroclastic flow
    extent from volcanic activity. Building footprints and structures within the mapped
    hazard zone were identified and counted to estimate direct damage, resulting in
    411 affected structures (260 in the main settlement).
  sources:
  - id: source_1
    license: null
    name: Copernicus EMS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UNITAR-UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from pyroclastic flow affecting 411 structures
      in San Miguel de Los Lotes and surrounding areas
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
  description: "Guatemala - Estimaci\xF3n del n\xFAmero de viviendas y estructuras\
    \ da\xF1adas en la aldea de San Miguel de Los Lotes y los alreadedores (Shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/GT/VO20180605GTM/VO20180605GTM_shp.zip
  format: null
  id: resource_3faa1536
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20180605GTM_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-gtm_unosat_estimaciondelnumerodevivi_20180607
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
  end: null
  start: '2018-06-07'
temporal_resolution: null
title: "Guatemala - Estimaci\xF3n del n\xFAmero de viviendas y estructuras da\xF1\
  adas en la aldea de San Miguel de Los Lotes y los alreadedores"
version: null
vulnerability: null
---
