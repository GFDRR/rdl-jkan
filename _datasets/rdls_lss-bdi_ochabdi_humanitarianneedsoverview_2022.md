---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/bdi_jiaf-1-1_and_hno2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/bdi_jiaf-1-1_and_hno2022
creator:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/bdi_jiaf-1-1_and_hno2022
dataset_id: rdls_lss-bdi_ochabdi_humanitarianneedsoverview_2022
description: 'This dataset presents key outputs and a step-by-step implementation
  of the Joint Intersectoral Analysis Framework(JIAF) approach in Burundi as well
  as the number of people in need ( PIN ) disaggregated by gender, age, population
  groups and geographical area. JIAF is a methodologically new approach to analysing
  the multiple needs of populations in crisis, their magnitude and severity.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bdi_jiaf-1-1_and_hno2022]'
details: A summary of JIAF methodology is available in the [Burundi HNO 2022](https://reliefweb.int/sites/reliefweb.int/files/resources/hno_2022-burundi_final.pdf).
  For more details, please contact OCHA office in Burundi.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Joint Intersectoral Analysis Framework (JIAF) 1.1 aggregates data
    from multiple humanitarian partners to analyze the magnitude and severity of needs
    across populations in crisis in Burundi. The framework produces people in need
    (PIN) estimates disaggregated by gender, age, population groups, and geographical
    area, representing total humanitarian impact across multiple sectors.
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
- href: https://data.humdata.org/dataset/bdi_jiaf-1-1_and_hno2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across multiple sectors due to crisis conditions in
      Burundi
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi - Humanitarian Needs Overview 2022(JIAF 1.1) (Excel)
  download_url: https://data.humdata.org/dataset/1204ecbb-64f8-4987-a4ed-8399c8b64fd9/resource/2521a422-a861-4418-b463-97851bdb75b5/download/burundi_hno2022_jiaf1_1.xlsx
  format: null
  id: resource_2521a422
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2022
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdi_ochabdi_humanitarianneedsoverview_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: Burundi - Humanitarian Needs Overview 2022(JIAF 1.1)
version: null
vulnerability: null
---
