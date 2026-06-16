---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/haiti-cible-hrp-2019-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-cible-hrp-2019-2020
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-cible-hrp-2019-2020
dataset_id: rdls_lss-hti_ochahti_ciblehrp20192020_20190130
description: 'This dataset is produced by the United Nations for the Coordination
  of Humanitarian Affairs (OCHA) in collaboration with humanitarian partners in Haiti.
  It contains the estimation of people aggregated per geographic locations, sex and
  age who have been targeted for urgent humanitarian response in Haiti. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/haiti-cible-hrp-2019-2020]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: OCHA Haiti compiled humanitarian response plan targeting data for 2019-2020
    by aggregating people in need estimates from multisector humanitarian partners,
    stratified by geographic administrative divisions, sex, and age groups to support
    humanitarian response planning and resource allocation.
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
- href: https://data.humdata.org/dataset/haiti-cible-hrp-2019-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People targeted for humanitarian response in Haiti, aggregated by
      geographic location, sex, and age
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.humanitarianresponse.info/en/operations/haiti/document/ha%C3%AFti-plan-de-r%C3%A9ponse-humanitaire-2019-2020-janvier-2019
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the estimation of people aggregated per geographic
    locations, sex and age who have been targeted for urgent humanitarian response
    in Haiti
  download_url: https://data.humdata.org/dataset/45544045-0601-4424-9d8e-ececefd889d0/resource/ee6b4c0c-6d2a-4d87-9f73-4ad34e79c66c/download/haiti-ciblage-hrp-2019-2020.xlsx
  format: null
  id: resource_ee6b4c0c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Haiti Ciblage HRP 2019-2020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_ciblehrp20192020_20190130
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-01-30'
temporal_resolution: null
title: Haiti Cible HRP 2019-2020
version: null
vulnerability: null
---
