---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mw-6-2-khost-province-earthquake-afghanistan-21-june-2022-unosat-live-web-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mw-6-2-khost-province-earthquake-afghanistan-21-june-2022-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mw-6-2-khost-province-earthquake-afghanistan-21-june-2022-unosat-live-web-map
dataset_id: rdls_hl-afg_unosat_mw62khostprovinceearthqua_20220630
description: 'UNOSAT code: EQ20220622AFG Live web map providing geospatial information
  about damaged caused by the earthquake that stroke Afghanistan on 21 June 2022.
  This web map gives an updated overview over potentially damaged and damaged buildings
  based on very high-resolution satellite images. Furthermore, the application also
  gives an overview over identified shelters.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mw-6-2-khost-province-earthquake-afghanistan-21-june-2022-unosat-live-web-map]'
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared very high-resolution satellite
    imagery acquired before and after the 21 June 2022 earthquake to identify notable
    changes in building structures. Damaged and potentially damaged buildings were
    manually delineated and classified based on visual interpretation of satellite
    imagery, with results delivered as geospatial vector data (geodatabase and shapefile
    formats).
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
- href: https://data.humdata.org/dataset/mw-6-2-khost-province-earthquake-afghanistan-21-june-2022-unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from satellite imagery analysis
      of the Mw 6.2 earthquake
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
  description: Mw 6.2 Khost Province Earthquake, Afghanistan, 21 June 2022 - UNOSAT
    Live Web Map (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/AF/EQ20220622AFG/EQ20220622AFG_gdb.zip
  format: Geodatabase
  id: resource_8da4c5ee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220622AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mw 6.2 Khost Province Earthquake, Afghanistan, 21 June 2022 - UNOSAT
    Live Web Map (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/AF/EQ20220622AFG/EQ20220622AFG_SHP.zip
  format: null
  id: resource_b213c3a0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220622AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_mw62khostprovinceearthqua_20220630
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-06-30'
temporal_resolution: null
title: Mw 6.2 Khost Province Earthquake, Afghanistan, 21 June 2022 - UNOSAT Live Web
  Map
version: null
vulnerability: null
---
