---
attributions:
- entity:
    affiliation: null
    email: null
    name: FEWS.net (Famine Early Warning Systems Network)
    url: https://data.humdata.org/dataset/nigeria-fewsnet-ipc-acute-food-security-classifications-over-time-2009-2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/nigeria-fewsnet-ipc-acute-food-security-classifications-over-time-2009-2018
creator:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/nigeria-fewsnet-ipc-acute-food-security-classifications-over-time-2009-2018
dataset_id: rdls_lss-nga_drew_fewsnetipcacutefoodsecuri_20180425
description: 'This report explores food insecurity in Nigeria in the context of urbanization
  and demographic change. A comparison of changing acute food security measures (IPC)
  from January and February 2010-2018 accompanies the report. The authors, Jordan
  Burnett, Leah Nadel, Victoria Santiago, and Arline Tarazona, completed their research
  in partial fulfillment of Public Health coursework in Medical Geography, for Spring
  2018, at Drew University. Dr. Lisa Jordan edited the report and supplemented their
  work with additional spatial data.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nigeria-fewsnet-ipc-acute-food-security-classifications-over-time-2009-2018]'
details: Lisa Jordan assembled the Nigeria data set, but the original source is FEWS
  NET. Please acknowledge FEWS.net for present and historical data using the IPC system
  to classify acute food security. Consult FEWS NET or IPCInfo for documentation on
  appropriate display of IPC classes.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS.net IPC acute food security classification shapefiles for Nigeria
    (2010-2018) were obtained and analyzed by Drew University researchers to characterize
    temporal trends in food insecurity phases across administrative regions. The dataset
    synthesizes historical IPC classifications to document changing patterns of food
    security status over an 8-year period in the context of urbanization and demographic
    change.
  sources:
  - id: source_1
    license: null
    name: FEWS.net (Famine Early Warning Systems Network)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nigeria-fewsnet-ipc-acute-food-security-classifications-over-time-2009-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food security classifications (IPC phases 1-5) for populations
      affected by food insecurity in Nigeria
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
  url: http://www.fews.net/data
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: http://www.ipcinfo.org/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'FEWS NET IPC Acute Food Security Classification for Nigeria (2009-2018)
    stored as shapefiles, by year and month (3-4 times annually). Attributes(s): CS:
    Current Status (IPC Value 1-5, or 99 for missing data or not monitored) HA0: the
    value 1 indicates that the situation would be worse on the IPC scale if not for
    humanitarian aid, 0 otherwise'
  download_url: https://data.humdata.org/dataset/60673af7-250a-41c4-9b48-ff25a8354f43/resource/240df655-3b21-4173-9ca1-f138e47cfa18/download/fewsnet_nga.zip
  format: null
  id: resource_240df655
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fewsnet_nga.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In the 'Food Security and Public Health Synthesis Report - Case Study
    of Nigeria,' Jordan Burnett, Leah Nadel, Victoria Santiago, and Arline Tarazona
    explore how urbanization, demography, and conflict are contributing factors in
    acute food insecurity.
  download_url: https://data.humdata.org/dataset/60673af7-250a-41c4-9b48-ff25a8354f43/resource/68f9e92c-ca47-42e7-bc12-1f2383adde16/download/food-security-and-public-health-synthesis-report-spring-2018.pdf
  format: null
  id: resource_68f9e92c
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food Security and Public Health Synthesis Report - Spring 2018.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria - FEWSNET IPC Acute Food Security Classifications over Time:
    A Public Health and Food Security Synthesis Report with Corresponding Data (Additional
    contact information and details regarding data and report.)'
  download_url: https://data.humdata.org/dataset/60673af7-250a-41c4-9b48-ff25a8354f43/resource/cee0b03b-f4fb-468d-afe5-b6b3ce440717/download/letter-to-hdx-community-regarding-accompanying-data-and-report-spring-2018.pdf
  format: null
  id: resource_cee0b03b
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Letter to HDX Community Regarding Accompanying Data and Report - Spring 2018.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_drew_fewsnetipcacutefoodsecuri_20180425
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-04-25'
temporal_resolution: null
title: 'Nigeria - FEWSNET IPC Acute Food Security Classifications over Time: A Public
  Health and Food Security Synthesis Report with Corresponding Data'
version: null
vulnerability: null
---
