---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/drc-severity-of-needs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-severity-of-needs
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-severity-of-needs
dataset_id: rdls_lss-cod_ochacod_severityneeds
description: "The dataset contains severity score of needs per 'zone de sant\xE9'\
  \ (admin level 3).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drc-severity-of-needs]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Severity of needs scores were compiled from multiple humanitarian\
    \ partner assessments and aggregated to zone de sant\xE9 (health zone, admin level\
    \ 3) administrative units. The methodology is documented in the 2021 HNO for DRC,\
    \ representing post-event or ongoing humanitarian impact assessment data."
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/drc-severity-of-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Severity of humanitarian needs per health zone derived from multi-source
      humanitarian partner assessments
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
  url: https://reliefweb.int/sites/reliefweb.int/files/resources/hno_2021-final_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Severity of Needs (Severity of needs
    - HNO 2021)'
  download_url: https://data.humdata.org/dataset/f3178bdb-e43c-4e4a-b60e-b2e77fd57944/resource/22aa12e7-ea7d-4aa3-bea6-6530f5b029a5/download/severite_hno_2021.xlsx
  format: null
  id: resource_22aa12e7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: severite_hno_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_severityneeds
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'Democratic Republic of the Congo: Severity of Needs'
version: null
vulnerability: null
---
