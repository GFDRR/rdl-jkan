---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/democratic-people-s-republic-of-korea-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/democratic-people-s-republic-of-korea-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/democratic-people-s-republic-of-korea-humanitarian-needs-overview
dataset_id: rdls_lss-prk_ocharoap_democraticpeoplesrepublic_20200210
description: 'This dataset contains the affected populations, people in need and targeted
  populations by sector and disaggregated by sex and age. The dataset is produced
  by the United Nations for the Coordination of Humanitarian Affairs (OCHA) in collaboration
  with humanitarian partners.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/democratic-people-s-republic-of-korea-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessment data collected
    by OCHA and humanitarian partners in DPR Korea through registry-based methodology.
    Population impact figures (affected, in need, targeted) are disaggregated by sector
    and demographics to support humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/democratic-people-s-republic-of-korea-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected populations and people in need by sector from humanitarian
      needs overview
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea : Humanitarian Needs Overview
    (Provisional data on people in need in the Democratic People''s Republic of Korea)'
  download_url: https://data.humdata.org/dataset/8085ce41-98dc-42dc-aedc-b5dc904a194b/resource/7267b407-3806-448c-8f78-f9b98cb8ed11/download/2020_dprk_np_overview_provisional_data.xlsx
  format: null
  id: resource_7267b407
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020_DPRK_N&P_Overview_Provisional_data.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-prk_ocharoap_democraticpeoplesrepublic_20200210
spatial:
  bbox: null
  centroid: null
  countries:
  - PRK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-02-10'
temporal_resolution: null
title: 'Democratic People''s Republic of Korea : Humanitarian Needs Overview'
version: null
vulnerability: null
---
