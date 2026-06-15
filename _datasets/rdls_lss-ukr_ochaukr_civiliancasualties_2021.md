---
attributions:
- entity:
    affiliation: null
    email: null
    name: Office of the High Commissioner for Human Rights (OHCHR)
    url: https://data.humdata.org/dataset/ukraine-civilian-casualties
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukraine-civilian-casualties
creator:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukraine-civilian-casualties
dataset_id: rdls_lss-ukr_ochaukr_civiliancasualties_2021
description: 'Dataset includes monthly numbers of civilian casualties by cause, type
  and location (adm1, GCA/NGCA) in 2021, and yearly numbers of civilian casualties
  by cause, type and location (GCA/NGCA) in 2016-2020. The dataset is compiled based
  on the monthly and yearly updates on civilian casualties in Ukraine provided by
  the Office of the High Commissioner for Human Rights (OHCHR).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ukraine-civilian-casualties]'
details: OHCHR documents civilian casualties by consulting a broad range of sources
  and types of information, which are evaluated for credibility and reliability. OHCHR
  updates on civilian casualties are based on information that the UN Human Rights
  Monitoring Mission in Ukraine (HRMMU) collected through interviews with victims
  and their relatives; witnesses; analysis of corroborating material confidentially
  shared with HRMMU; official records; open-source documents, photo and video materials;
  forensic records and reports; criminal investigation materials; court documents;
  public reports of the OSCE Special Monitoring Mission to Ukraine; reports by international
  and national non-governmental organizations; public reports by law enforcement and
  military actors; data from medical facilities and local authorities; and other relevant
  and credible material. In some instances, corroboration may take weeks or months
  before conclusions can be drawn. This may mean that conclusions on civilian casualties
  may be revised as more information becomes available and numbers may change as new
  information emerges over time.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly and yearly civilian casualty figures were compiled directly
    from OHCHR observational reports covering 2016-2021, disaggregated by cause of
    death/injury, casualty type, and geographic location (administrative level 1 and
    GCA/NGCA status). Data represents direct observational/anecdotal records of conflict-related
    civilian impacts.
  sources:
  - id: source_1
    license: null
    name: Office of the High Commissioner for Human Rights (OHCHR)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-civilian-casualties
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct civilian deaths from conflict-related violence by cause and
      location
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
    description: Direct civilian injuries from conflict-related violence by cause
      and location
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
        metric: ppl_injured
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset includes monthly numbers of civilian casualties by cause, type
    and location (adm1, GCA/NGCA) in 2021, and yearly numbers of civilian casualties
    by cause, type and location (GCA/NGCA) in 2016-2020.
  download_url: https://data.humdata.org/dataset/36adea79-8675-4f19-a035-7fa07ca1fc11/resource/a7440a59-e4ef-4050-a155-aaf332e04577/download/2021-10-05-hdx-civilian-casualties.xlsx
  format: null
  id: resource_a7440a59
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine_civilian casualties_2016-2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_ochaukr_civiliancasualties_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-09-30'
  start: '2021-01-01'
temporal_resolution: null
title: 'Ukraine: Civilian Casualties'
version: null
vulnerability: null
---
