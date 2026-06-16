---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/honduras-pin-hno-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Joint and Intersectoral Analysis Framework (JIAF)
    url: https://data.humdata.org/dataset/honduras-pin-hno-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-pin-hno-2022
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-pin-hno-2022
dataset_id: rdls_lss-hnd_ocharolac_humanitarianneedsoverview_2023
description: 'This data has been produced by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. The data provides the Humanitarian Country Team''s shared understanding
  of the crisis, including the most pressing humanitarian need and the estimated number
  of people who need assistance. It represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-pin-hno-2022]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Humanitarian Needs Overview was produced by UNOCHA and humanitarian
    partners using the Joint and Intersectoral Analysis Framework (JIAF) to consolidate
    evidence on humanitarian needs and estimate people in need (PIN) across Honduras.
    The dataset represents a shared understanding of the crisis to inform joint strategic
    response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Joint and Intersectoral Analysis Framework (JIAF)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-pin-hno-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need due to flood-related humanitarian crisis in Honduras
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
  description: The dataset contains information on the number of people in need in
    Honduras in 2023 at the admin 2 level.
  download_url: https://data.humdata.org/dataset/28039bc2-484b-474b-8fb0-29fee1ec12bb/resource/c1ebd315-c5b5-4087-aec1-9763c99c0dcd/download/honduras-pin-hno-2022-.csv
  format: null
  id: resource_c1ebd315
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: honduras-pin-hno-2023.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_ocharolac_humanitarianneedsoverview_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: 'Honduras: Humanitarian Needs Overview'
version: null
vulnerability: null
---
