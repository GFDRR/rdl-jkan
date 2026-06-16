---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA South Sudan
    url: https://data.humdata.org/dataset/ssd-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/ssd-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/ssd-humanitarian-needs-overview
dataset_id: rdls_lss-ssd_hdx_humanitarianneedsoverview_202101
description: 'South Sudan Humanitarian needs overview for 2021. This data has been
  extracted from the published HNO document for South Sudan. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ssd-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Humanitarian Needs Overview (HNO) for South Sudan 2021 was compiled
    by OCHA South Sudan through sample survey methodology to assess humanitarian needs
    and affected populations. The dataset extracts key impact figures from the published
    HNO document to quantify people in need across the country.
  sources:
  - id: source_1
    license: null
    name: OCHA South Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ssd-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need affected by humanitarian crisis including flood-related
      impacts in South Sudan
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Humanitarian needs overview (South Sudan Humanitarian
    needs overview)'
  download_url: https://data.humdata.org/dataset/a98aca08-3e9f-4108-82d2-53e7df37742c/resource/cf6f622e-a904-47f8-897e-a500507c70b4/download/south_sudan_2021_humanitarian_needs_overview.xlsx
  format: null
  id: resource_cf6f622e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: south_sudan_2021_humanitarian_needs_overview.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_hdx_humanitarianneedsoverview_202101
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-01-30'
  start: '2021-01-01'
temporal_resolution: null
title: 'South Sudan: Humanitarian needs overview'
version: null
vulnerability: null
---
