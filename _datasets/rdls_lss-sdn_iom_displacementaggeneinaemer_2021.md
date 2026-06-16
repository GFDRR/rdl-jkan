---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-displacement-ag-geneina-emergency-event-tracking-idps-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-displacement-ag-geneina-emergency-event-tracking-idps-iom-dtm
dataset_id: rdls_lss-sdn_iom_displacementaggeneinaemer_2021
description: 'The DTM Emergency Event Tracking (EET) is deployed to track sudden displacement
  and population movements, provide more frequent updates n the scale of displacement
  and quantify the affected population when needed.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/sudan-displacement-ag-geneina-emergency-event-tracking-idps-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM Emergency Event Tracking deploys rapid assessment teams to
    document sudden displacement events in Ag Geneina, Sudan, recording displacement
    scale and affected population counts across multiple rounds (R1-R25) to provide
    frequent updates on population movements during emergencies.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-displacement-ag-geneina-emergency-event-tracking-idps-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from sudden displacement events tracked
      through Emergency Event Tracking
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
  description: Sudan Displacement - Ag Geneina - Emergency Event Tracking - IDPs [IOM
    DTM] (DTM Sudan Ag_Geneina Emergency Event Tracking R1 to R25)
  download_url: https://data.humdata.org/dataset/ebfb820b-7e32-4751-9ec8-7ee9d0cca63d/resource/0e717355-8a23-4b29-b8cc-b65ff76f69c3/download/hdx_dtm_eet_dataset_2021.xlsx
  format: null
  id: resource_0e717355
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Sudan Ag_Geneina Emergency Event Tracking R1 to R25
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan Displacement - Ag Geneina - Emergency Event Tracking - IDPs [IOM
    DTM] (DTM Sudan Ag_Geneina Emergency Event Tracking R8)
  download_url: https://data.humdata.org/dataset/ebfb820b-7e32-4751-9ec8-7ee9d0cca63d/resource/7c004a37-617c-4e4e-9c61-dab79d4ab6ae/download/dtm-sudan-ag_geneina-emergency-event-tracking-r8.xlsx
  format: null
  id: resource_7c004a37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Sudan Ag_Geneina Emergency Event Tracking R8
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_iom_displacementaggeneinaemer_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-22'
  start: '2021-02-24'
temporal_resolution: null
title: Sudan Displacement - Ag Geneina - Emergency Event Tracking - IDPs [IOM DTM]
version: null
vulnerability: null
---
