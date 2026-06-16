---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1
dataset_id: rdls_lss-cmr_unhcr_farnorthjointassessmentni_202111
description: 'UNHCR-WFP joint assessment mission (JAM) of Nigerian refugees in the
  Far North of Cameroon carried out between October 7 and 19, 2021. The objective
  of the assessment was to collect updated information on basic needs, shelter, food
  security, nutrition, water and sanitation, education, protection, security, common
  services, and livelihoods of Nigerian refugees to inform improved humanitarian assistance.
  This dataset contains data collected from samples of 607 out of approximately 10,000
  households hosting 60,000 refugees in the Minawao settlement and 435 from close
  to 11,000 households hosting 57,000 refugees in host villages in surrounding border
  areas. The majority of the Nigerian Refugees in this Region fled violence and attacks
  perpetrated by Non-State Armed Groups (NSAGs) such as Boko-Haram in the Neighboring
  Nigeria since 2014. The report published in September 2022 reveals interesting findings
  such as the difference in dependency ratios between the refugees in camps and those
  living in the host population. Additionally, comparative analysis on indicators
  such as the Food Consumption Score (FCS) and the reduced Coping Strategy Index (rCSI)
  between the two (02) groups are conducted and yield some interesting findings..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Sample survey data collected via face-to-face interviews from 607 households
    in Minawao settlement and 435 households in host communities during October 7-19,
    2021. Data aggregated from UNHCR-WFP joint assessment mission to document humanitarian
    needs, food security status, and protection concerns of Nigerian refugee populations
    displaced by conflict in the Far North Region of Cameroon.
  sources:
  - id: source_1
    license: null
    name: UNHCR
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
- href: https://data.humdata.org/dataset/unhcr-cmr-2021-jam-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and basic needs impact among Nigerian refugee population
      affected by conflict-related displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/676/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_6c2dc5b5
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cameroon - Far North Joint Assessment of Nigerian Refugees - Nov 2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon - Far North Joint Assessment of Nigerian Refugees - Nov 2021
    (Contains information about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/676/pdf-documentation
  format: null
  id: resource_317f8e66
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
slug: rdls_lss-cmr_unhcr_farnorthjointassessmentni_202111
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-11-19'
  start: '2021-11-07'
temporal_resolution: null
title: Cameroon - Far North Joint Assessment of Nigerian Refugees - Nov 2021
version: null
vulnerability: null
---
