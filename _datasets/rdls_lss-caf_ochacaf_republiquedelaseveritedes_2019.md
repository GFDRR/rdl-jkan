---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/republique-de-la-centrafrique-severite-des-besoins
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/republique-de-la-centrafrique-severite-des-besoins
creator:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/republique-de-la-centrafrique-severite-des-besoins
dataset_id: rdls_lss-caf_ochacaf_republiquedelaseveritedes_2019
description: "Ce jeu de donn\xE9es porte sur la s\xE9v\xE9rit\xE9 des besoins dans\
  \ plusieurs secteurs dont la sant\xE9, l'\xE9ducation, la nutrition, la s\xE9curit\xE9\
  \ alimentaire et la protection.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/republique-de-la-centrafrique-severite-des-besoins]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs severity data aggregated from multiple humanitarian
    partners across five sectors (health, education, nutrition, food security, protection)
    in Central African Republic. The dataset classifies affected populations by severity
    level based on multi-sector humanitarian response information compiled for the
    2022 Humanitarian Needs Overview.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/republique-de-la-centrafrique-severite-des-besoins
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population severity classification across health, education,
      nutrition, food security and protection sectors
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  url: https://www.humanitarianresponse.info/sites/www.humanitarianresponse.info/files/documents/files/hno_car_2022_final.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique de la Centrafrique: S\xE9\
    v\xE9rit\xE9 des besoins (Excel)"
  download_url: https://data.humdata.org/dataset/56506603-039f-4ec7-9b8b-52f03764499e/resource/d6400ec5-55e6-4768-90a5-022f7c35577f/download/severite_cluster.xlsx
  format: null
  id: resource_d6400ec5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SEVERITE_CLUSTER.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_ochacaf_republiquedelaseveritedes_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: "Central African Republic - R\xE9publique de la Centrafrique: S\xE9v\xE9rit\xE9\
  \ des besoins"
version: null
vulnerability: null
---
