---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/malawi-flood-fl-20230301-mwi-02
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/malawi-flood-fl-20230301-mwi-02
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/malawi-flood-fl-20230301-mwi-02
dataset_id: rdls_hl-mwi_wfpadam_flood1110440sqmmar2023_20230301
description: 'ADAM ID: FL-20230301-MWI-02 Flood covering 111044.0 sq m on Mar 01 2023
  in Malawi. It impacted 233237 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-flood-fl-20230301-mwi-02]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "WFP ADAM system collected and mapped observed flood extent (0.111\
    \ km\xC2\xB2) and documented affected population (233,237 people) following the\
    \ 1 March 2023 flood event in Malawi. The dataset represents post-event impact\
    \ assessment from an operational emergency response system."
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-flood-fl-20230301-mwi-02
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood event on 1 March 2023
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: 'Malawi: Flood - 111044.0 sq m - Mar 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/9846da9f-83e5-4146-8726-577d22aa9ab5/resource/0f2b0b95-925f-44ca-ad73-c1e0837d1786/download/metadata.txt
  format: null
  id: resource_0f2b0b95
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: metadata.txt
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mwi_wfpadam_flood1110440sqmmar2023_20230301
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-01'
temporal_resolution: null
title: 'Malawi: Flood - 111044.0 sq m - Mar 2023'
version: null
vulnerability: null
---
