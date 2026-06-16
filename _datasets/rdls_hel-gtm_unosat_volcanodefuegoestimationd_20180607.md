---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Emergency Management Service (EMS)
    url: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-
dataset_id: rdls_hel-gtm_unosat_volcanodefuegoestimationd_20180607
description: 'This map illustrates an estimation of the number of buildings potentially
  affected by pyroclastic flow detected by Copernicus EMS using a Sentinel-2 satellite
  image collected on 4 June 2018. UNITAR-UNOSAT estimates 411 buildings / structures
  within the pyroclastic flow, ~ 260 of which are located inside the community of
  San Miguel de Los Lotes. Industrial sites and the resort of La Reunion are also
  included in the extent of this pyroclastic flow. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-]'
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
    description: Building stock within pyroclastic flow extent in San Miguel de Los
      Lotes and surrounding area
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
hazard:
  event_sets_by_hazard_type:
    volcanic:
    - analysis_type: empirical
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
  description: "Sentinel-2 satellite imagery from 4 June 2018 was analyzed by Copernicus\
    \ EMS to delineate the pyroclastic flow extent from the Volc\xE1n de Fuego eruption.\
    \ UNITAR-UNOSAT then conducted a spatial overlay analysis to estimate the number\
    \ of buildings and structures intersecting the pyroclastic flow polygon, identifying\
    \ 411 affected buildings including residential structures in San Miguel de Los\
    \ Lotes, industrial sites, and the La Reunion resort. This preliminary assessment\
    \ was not validated in the field."
  sources:
  - id: source_1
    license: null
    name: Copernicus Emergency Management Service (EMS)
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
- href: https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: "Estimated count of buildings affected by pyroclastic flow from Volc\xE1\
      n de Fuego"
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
  description: 'Volcano de Fuego: Estimation of damaged buildings in San Miguel de
    Los Lotes and surrouding area, Guatemala (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/GT/VO20180605GTM/VO20180605GTM_shp.zip
  format: null
  id: resource_cf36a3f6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20180605GTM_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-gtm_unosat_volcanodefuegoestimationd_20180607
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
title: 'Volcano de Fuego: Estimation of damaged buildings in San Miguel de Los Lotes
  and surrouding area, Guatemala'
version: null
vulnerability: null
---
