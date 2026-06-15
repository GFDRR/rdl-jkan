---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview
dataset_id: rdls_lss-pak_ochapak_humanitarianneedsoverview_2021
description: 'This dataset contains the people in need by sector and area. The dataset
  is produced by the United Nations for the Coordination of Humanitarian Affairs (OCHA)
  in collaboration with humanitarian partners.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview]'
details: The HNO is compiled by OCHA from input received from clusters/sectors and
  partners in-country
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset aggregates people in need estimates by sector and geographic
    area collected through direct observational data and anecdotal reports from multiple
    humanitarian partners coordinated by OCHA Pakistan. Data was compiled into a consolidated
    humanitarian needs overview to support humanitarian response planning and resource
    allocation.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pakistan-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need by sector affected by humanitarian crisis including
      flood-related impacts
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Humanitarian Needs Overview (Pakistan Humanitarian Needs
    Overview 2021)'
  download_url: https://data.humdata.org/dataset/a6f0f0ce-83ef-465b-8b3b-a7cb36dd1a94/resource/d20b1642-e6de-4bc1-9315-81a32eb88c3a/download/pak_hno_2021.xlsx
  format: null
  id: resource_d20b1642
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PAK_HNO_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pak_ochapak_humanitarianneedsoverview_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Pakistan: Humanitarian Needs Overview'
version: null
vulnerability: null
---
