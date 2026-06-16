---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-for-chido-25-in-mozambique
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-for-chido-25-in-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-for-chido-25-in-mozambique
dataset_id: rdls_hel-moz_unosat_livewebmaptropicalcyclone_20241213
description: 'UNOSAT code: TC20241212MOZ, GDACS ID: 1001131 This application provides
  flood impact assessments for related to the Tropical Cyclone for CHIDO-25 in Mozambique.
  Important note: The boundaries and names shown, and the designations used on this
  map do not imply official endorsement or acceptance by the United Nations. The designations
  employed and the presentation of material on this map do not imply the expression
  of any opinion whatsoever on the part of the Secretariat of the United Nations concerning
  the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-for-chido-25-in-mozambique]'
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
    description: Population exposed to tropical cyclone impacts in affected areas
      of Mozambique
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
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery before and after Tropical
    Cyclone CHIDO-25 to identify flood impacts and assess population exposure in Mozambique.
    Population exposure analysis was conducted by overlaying flood-affected areas
    with gridded population data to quantify affected populations.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-for-chido-25-in-mozambique
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone CHIDO-25 flood impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
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
  description: UNOSAT Live Web Map Tropical Cyclone for CHIDO-25 in Mozambique (Excel
    file)
  download_url: https://unosat.org/static/unosat_filesystem/4049/UNOSAT_PopulationExposureAnalysis_CHIDO25_Mozambique_13122024.xlsx
  format: null
  id: resource_95a61e70
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_CHIDO25_Mozambique_13122024.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_unosat_livewebmaptropicalcyclone_20241213
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-13'
temporal_resolution: null
title: UNOSAT Live Web Map Tropical Cyclone for CHIDO-25 in Mozambique
version: null
vulnerability: null
---
