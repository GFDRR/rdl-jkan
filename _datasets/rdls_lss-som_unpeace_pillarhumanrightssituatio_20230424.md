---
attributions:
- entity:
    affiliation: null
    email: null
    name: Secretary General's Report on the situation in Somalia
    url: https://data.humdata.org/dataset/unsom-sgrhumanrights
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Peace and Security Data Hub
  url: https://data.humdata.org/dataset/unsom-sgrhumanrights
creator:
  affiliation: null
  email: null
  name: United Nations Peace and Security Data Hub
  url: https://data.humdata.org/dataset/unsom-sgrhumanrights
dataset_id: rdls_lss-som_unpeace_pillarhumanrightssituatio_20230424
description: 'This dataset was last updated in April 2023 and will no longer receive
  updates. Historical data remains available for reference. This dataset is an extraction
  of information from the Secretary General''s Report on the situation in Somalia
  (SG reports) since 2013. It provides quarterly total of civilian casualties, fatalities,
  persons arbitrarily arrested, children subject to grave violations, to reflect the
  country''s human rights situation.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unsom-sgrhumanrights]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Quarterly human rights impact data extracted from UN Secretary General
    reports on Somalia since 2013, documenting civilian casualties, fatalities, arbitrary
    arrests, and grave violations against children and survivors of sexual and gender-based
    violence to track the humanitarian consequences of the complex emergency and conflict
    situation.
  sources:
  - id: source_1
    license: null
    name: Secretary General's Report on the situation in Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unsom-sgrhumanrights
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Civilian fatalities from conflict-related incidents in Somalia
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian casualties (injured and affected) from conflict-related
      incidents in Somalia
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
  - asset_category: population
    asset_dimension: population
    description: Persons arbitrarily arrested due to conflict and security situation
      in Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: 'Peace and Security Pillar: Human Rights Situation in Somalia, Data
    From Secretary General Reports (CSV)'
  download_url: https://data.humdata.org/dataset/7bdb1096-0055-4cb1-b8fd-62e0af8ed75b/resource/f33ef631-ab4b-42d4-aa12-62d9affd4e40/download/unsom-sgrhumanrights.csv
  format: null
  id: resource_f33ef631
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: unsom-sgrhumanrights.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_unpeace_pillarhumanrightssituatio_20230424
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-04-24'
temporal_resolution: null
title: 'Peace and Security Pillar: Human Rights Situation in Somalia, Data From Secretary
  General Reports'
version: null
vulnerability: null
---
