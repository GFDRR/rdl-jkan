---
attributions:
- entity:
    affiliation: null
    email: null
    name: Safeguarding Health in Conflict Coalition (SHCC)
    url: https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Insecurity Insight
  url: https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare
creator:
  affiliation: null
  email: null
  name: Insecurity Insight
  url: https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare
dataset_id: rdls_lss-pse_insecinsight_statepseattacksaidoperati_2016
description: 'This page contains information on reported incidents of violence and
  threats affecting aid operations and workers, education, food and water systems,
  health care services and refugee and IDP camps in the oPt . They also provide information
  on incidents of conflict related sexual violence (CRSV) and explosive weapons use
  affecting aid access, education, food security and health care services. Also included
  are datasets cited in the Safeguarding Health in Conflict Coalition (SHCC)''s annual
  reports. Please get in touch if you are interested in curated datasets: info@insecurityinsight.org.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare]'
details: The incidents reported are not a complete nor a representative list of all
  incidents and have not been independently verified.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Post-event incident data systematically collected from open source
    reports and verified submissions from partner agencies documenting attacks on
    aid operations, health facilities, education infrastructure, food and water systems,
    and protection sites in the occupied Palestinian territory from 2016-2025. Data
    includes casualty figures, facility damage assessments, and worker safety incidents
    compiled by Insecurity Insight and the Safeguarding Health in Conflict Coalition.
  sources:
  - id: source_1
    license: null
    name: Insecurity Insight
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Safeguarding Health in Conflict Coalition (SHCC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Attacks on food and water systems infrastructure during conflict
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Attacks on health care facilities and education facilities
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Health workers killed, injured, kidnapped, arrested, threatened,
      assaulted and sexually assaulted
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Incidents affecting IDP and refugee camps
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Resource covering 07 October 2023-30 September 2025 on food-related
    violence based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/c0aa8ef5-b601-4ada-be9e-13b17b791ad0/download/2023-2025-pse-gaza-conflict-incidents-affecting-food-systems-incident-data-incident-data.xlsx
  format: null
  id: resource_c0aa8ef5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2025 PSE (Gaza) Conflict Incidents Affecting Food Systems Incident Data
    Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 01 January 2020 to 05 July 2025 on aid workers killed,
    injured, kidnapped, or arrested (KIKA) based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/7c42af43-e847-4793-aa66-bc66e1849f0d/download/2020-2025-pse-aid-worker-kika-incident-data.xlsx
  format: null
  id: resource_7c42af43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020-2025-PSE Aid Worker KIKA Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 01 January 2016 to 26 June 2025 on attacks on health
    care based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/5adcd4f5-8432-458b-a435-b994ab6913e2/download/2016-2025-pse-attacks-on-health-care-incident-data.xlsx
  format: null
  id: resource_5adcd4f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2016-2025-PSE Attacks on Health Care Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 01 January 2020 to 12 March 2025 on publicly-reported
    incidents of sexual violence perpetrated by conflict actors, security personnel,
    and sexual violence that targets aid workers, educators, health workers and IDPs/refugees.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/88daa748-a867-4f33-a5b0-4bfec6f8c763/download/2023-2025-pse-conflict-related-sexual-violence-incident-data.xlsx
  format: null
  id: resource_88daa748
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2025-PSE Conflict Related Sexual Violence Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 01 January 2020 to 05 July 2025 on incidents in which
    aid access, education and healthcare services were impacted by explosive weapons
    based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/6d9fcb93-0136-44ed-a11a-693ac892f4ab/download/2020-2025-pse-explosive-weapons-incident-data.xlsx
  format: null
  id: resource_6d9fcb93
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020-2025-PSE Explosive Weapons Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 16 October 2023 to 05 July 2025 on incidents with
    clearly foreseeable impacts on or links to food security based on agency- and
    open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/d4586c59-6bdb-497d-9fe1-0d6e1b439e81/download/2021-2025-pse-food-security-incident-data.xlsx
  format: null
  id: resource_d4586c59
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021-2025-PSE Food Security Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering January 2020 to 29 June 2025 on threats and violence
    at IDP/refugee camps based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/d772fcfa-a9fe-44ea-9c0c-9bedd65bc224/download/2020-2025-pse-protection-in-danger-incident-data.xlsx
  format: null
  id: resource_d772fcfa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020-2025-PSE Protection in Danger Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covering 01 January 2020 to 26 June 2024 on attacks on education
    based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/0193c2ca-5859-401d-bdc9-5b184e976255/download/2020-2024-pse-education-in-danger-incident-data.xlsx
  format: null
  id: resource_0193c2ca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020-2024-PSE Education in Danger Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in 2024 identified by the Safeguarding Health in Conflict Coalition
    (SHCC) and cited in the report Epidemic of Violence . Read the factsheet
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/dbe8462e-ea26-43ab-8d04-0b67e90c7654/download/2023-2024-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_dbe8462e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2024 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in oPt in 2023 identified by the Safeguarding Health in Conflict
    Coalition (SHCC) and cited in the report Critical Conditions . Read the factsheet
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/13f16126-10a4-4860-bee6-947a9cb09719/download/2023-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_13f16126
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dataset contains reported incidents of violence against or obstruction
    of healthcare in Sudan in 2022 identified by the Safeguarding Health in Conflict
    Coalition (SHCC) and cited in the report ''Ignoring Red Lines''. Read the factsheet:
    https://shcc.pub/OPT2022 (EN) and https://shcc.pub/OPT2022AR (AR)'
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/777796b4-2163-4872-8ce2-4f2f2ff62cfd/download/2022-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_777796b4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of health care in OPT in 2021 identified by the Safeguarding Health in Conflict
    Coalition (SHCC).
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/f91654cb-2466-40d1-9d76-cc6194557f03/download/2021-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_f91654cb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in oPt in 2020 identified by the Safeguarding Health in Conflict
    Coalition (SHCC).
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/3fbf5373-3efd-4897-8828-566033e073f0/download/2020-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_3fbf5373
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in oPt in 2019 identified by the Safeguarding Health in Conflict
    Coalition (SHCC).
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/2fae26ad-dce5-4c3f-9696-08626b2b9d09/download/2019-pse-shcc-health-care-data.xlsx
  format: null
  id: resource_2fae26ad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2019 PSE SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Resource covering 07 October 2023-30 September 2025 on food-related
    violence based on agency- and open source events.
  download_url: https://data.humdata.org/dataset/b36e1975-4428-4caa-9b00-e0d8793130d0/resource/4058bcd6-0a96-4d66-889b-427b95fac5bb/download/2023-2025-pse-gaza-conflict-incidents-affecting-food-systems-incident-data-incident-data.xlsx
  format: null
  id: resource_4058bcd6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2025 PSE (Gaza) Conflict Incidents Affecting Food Systems Incident Data
    Incident Data.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_insecinsight_statepseattacksaidoperati_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '2016-01-01'
temporal_resolution: null
title: 'State of Palestine (PSE): Attacks on Aid Operations, Education, Food and Water
  Systems, Health Care and IDP/Refugee Camps, and Conflict-Related Sexual Violence
  and Explosive Weapons Incident Data'
version: null
vulnerability: null
---
