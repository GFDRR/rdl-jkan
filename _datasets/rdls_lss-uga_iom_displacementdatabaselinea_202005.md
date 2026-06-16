---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) DTM
    url: https://data.humdata.org/dataset/uganda-displacement-data-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/uganda-displacement-data-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/uganda-displacement-data-baseline-assessment-iom-dtm
dataset_id: rdls_lss-uga_iom_displacementdatabaselinea_202005
description: 'The dataset contains number of IDPs, Returnees (households and individuals)
  at sub national levels.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/uganda-displacement-data-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted a baseline assessment using standard DTM methodology
    to enumerate internally displaced persons and returnees (households and individuals)
    across sub-national administrative divisions in Uganda, producing displacement
    impact counts at the baseline period.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) DTM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/uganda-displacement-data-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees counted at sub-national
      level
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
        metric: displaced
        modelling: observed
        type: total
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
  description: A total of 248,210 individuals were affected by the floods in seven
    districts and 73 sub-counties. These make up approximately 37,000 households.
    Of these, 53% or 132,345 persons were displaced (approximately 20,805 households).
    Of the total displaced persons, 11% (14,206) had been displaced outside of their
    sub-county of habitual residence. Kasese was the district in which most people
    were affected (33%), but Bundibugyo had the highest displacement (49%). At the
    time of assessment 59,896 persons (8,720 households) had returned to their place
    of residence; these made up roughly 24 per cent of all affected people.
  download_url: https://data.humdata.org/dataset/47a9b677-be48-4bc9-a696-e6f39b524420/resource/f1f6b051-e63b-4c99-94fa-e2ac23dc5a56/download/hdx_uga_baseline_assessment_may_2020_round_1.xlsx
  format: null
  id: resource_f1f6b051
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Uganda Baseline Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-uga_iom_displacementdatabaselinea_202005
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-05-28'
  start: '2020-05-04'
temporal_resolution: null
title: Uganda Displacement Data - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
