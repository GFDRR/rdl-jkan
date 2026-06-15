---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-wipha-25-in-lao-pdr-and-viet-nam
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-wipha-25-in-lao-pdr-and-viet-nam
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-wipha-25-in-lao-pdr-and-viet-nam
dataset_id: rdls_hel-laovnm_unosat_livewebmaptropicalcyclone_20250722
description: 'UNOSAT code: TC20250722VNM, GDACS ID: 1001181 This application provides
  impact assessments of Tropical Cyclone WIPHA-25 in Lao PDR and Viet Nam.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-wipha-25-in-lao-pdr-and-viet-nam]'
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
    description: Population exposed to Tropical Cyclone WIPHA-25 impacts
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
  event_sets_by_hazard_type:
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery before and
    after Tropical Cyclone WIPHA-25 to identify notable changes and assess impacts
    on population exposure in Lao PDR and Viet Nam. The resulting impact assessment
    dataset integrates satellite-derived observations with population data to quantify
    affected populations.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-tropical-cyclone-wipha-25-in-lao-pdr-and-viet-nam
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Tropical Cyclone WIPHA-25 in Lao PDR and Viet
      Nam
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
  description: UNOSAT Live web map - Tropical Cyclone WIPHA-25 in LAO PDR and Viet
    Nam (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4150/UNOSAT_PopulationExposure_WiphaCyclone_22July2025_VietNam.xlsx
  format: null
  id: resource_7d0ac35e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_WiphaCyclone_22July2025_VietNam.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-laovnm_unosat_livewebmaptropicalcyclone_20250722
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-22'
temporal_resolution: null
title: UNOSAT Live web map - Tropical Cyclone WIPHA-25 in LAO PDR and Viet Nam
version: null
vulnerability: null
---
