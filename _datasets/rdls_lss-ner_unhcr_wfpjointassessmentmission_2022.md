---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/unhcr-ner-2022-jam-v2-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-ner-2022-jam-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-ner-2022-jam-v2-1
dataset_id: rdls_lss-ner_unhcr_wfpjointassessmentmission_2022
description: "In 2022, Niger totalled more than 700.000 displaced population of which\
  \ 250000 plus were refugees and asylum seekers. In the meantime, the country suffered\
  \ an unprecedented food crisis. In these settings, the UNHCR and WFP carried-out\
  \ between October 12 and November 4th, 2022, a joint assessment mission (JAM) to\
  \ assess the situation and provide support to refugees, asylum seekers, internally\
  \ Displaced (IDPs) and Host community members in the four regions of Diffa, Maradi,\
  \ Tahoua, and Tillab\xE9ri in Niger. The data was collected from about 4600+ households\
  \ with the specific objectives of assessing the basic needs, shelter, food security,\
  \ nutrition, water and sanitation, education, protection, security, common services,\
  \ and livelihoods of forcible displaced people to inform and improve humanitarian\
  \ assistance.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-ner-2022-jam-v2-1]"
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Sample survey data collected from 4,600+ households across four regions\
    \ of Niger (Diffa, Maradi, Tahoua, Tillab\xE9ri) through face-to-face interviews\
    \ conducted jointly by UNHCR and WFP between October 12 and November 4, 2022.\
    \ The assessment targeted refugees, asylum seekers, internally displaced persons,\
    \ and host community members to evaluate food security, health, nutrition, livelihoods,\
    \ and protection needs in response to displacement crises and food insecurity."
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WFP
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-ner-2022-jam-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and humanitarian needs affecting displaced populations
      and host communities
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and refugee populations in Niger
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/945/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_02d00819
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Niger - UNHCR/WFP Joint Assessment Mission in the regions of Diffa, Marradi,\
    \ Tahoua,Tillab\xE9ri - Niger 2022"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger - UNHCR/WFP Joint Assessment Mission in the regions of Diffa,\
    \ Marradi, Tahoua,Tillab\xE9ri - Niger 2022 (Contains information about the dataset's\
    \ metadata and data)"
  download_url: https://microdata.unhcr.org/index.php/catalog/945/pdf-documentation
  format: null
  id: resource_f651e63d
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_unhcr_wfpjointassessmentmission_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-11-04'
  start: '2022-10-12'
temporal_resolution: null
title: "Niger - UNHCR/WFP Joint Assessment Mission in the regions of Diffa, Marradi,\
  \ Tahoua,Tillab\xE9ri - Niger 2022"
version: null
vulnerability: null
---
