---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners in Iraq
    url: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Iraq (inactive)
  url: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Iraq (inactive)
  url: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview
dataset_id: rdls_lss-irq_ochairq_humanitarianneedsoverview_2022
description: 'The dataset is produced by the United Nations for the Coordination of
  Humanitarian Affairs (OCHA) in collaboration with humanitarian partners. It presents
  the number of people in need (PIN), the number of people in acute need (Acute PIN),
  the number of beneficiaries to be targeted for assitance, and the details of the
  activities under the 2022 HRP. The data sources and methodology for the derivation
  of the PIN and Acute PIN figures can be found in the Iraq 2022 HNO; the basis of
  the targets and further background and details of the HRP activities can be found
  in the Iraq 2022 HRP.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview]'
details: Humanitarian partners and sectors who provided input into the development
  of the Iraq 2022 planning figures are mentioned in the [Iraq 2022 HNO document](https://reliefweb.int/report/iraq/iraq-humanitarian-needs-overview-2022-march-2022)
  and [Iraq 2022 HRP document](https://reliefweb.int/report/iraq/iraq-humanitarian-response-plan-2022-march-2022).
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates people-in-need (PIN) and acute PIN figures derived
    from direct observational data and anecdotal reports collected by humanitarian
    partners operating in Iraq, compiled by OCHA for the 2022 Humanitarian Needs Overview
    and Response Plan. Data spans 2015-2022 with severity classifications and targeting
    information for humanitarian assistance activities.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners in Iraq
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iraq-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need (PIN) and acute need figures from humanitarian assessment
      in Iraq
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (IRAQ 2022 HNO HRP Population PIN
    Severity Targets Activities Requirements.xlsx)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/ca984a7a-d4a3-4e33-aaab-b4055627db90/download/iraq-2022-hno-hrp-population-pin-severity-targets-activities-requirements.xlsx
  format: null
  id: resource_ca984a7a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRAQ 2022 HNO HRP Population PIN Severity Targets Activities Requirements.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (Iraq 2021 Humanitarian Needs Overview
    and Response Plan Figures)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/1ba1112e-9e05-4e93-8135-d99202594354/download/iraq-hrp-2021-pin-targets-activity-data-compiled-p-coded.xlsx
  format: null
  id: resource_1ba1112e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iraq-hrp-2021-pin-targets-activity-data-compiled P-coded.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (Iraq 2021 Humanitarian Needs Overview
    and Response Plan Figures ADM1)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/d5d3d195-39d3-4868-b610-4d0f665aaaaf/download/irq_hrp_2021.csv
  format: null
  id: resource_d5d3d195
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_hrp_2021.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq 2020 HNO PIN, Acute PIN, and Severity - Estimates of the people
    in need and severity were derived from the Multi-Cluster Needs Assessment XII
    (2019) findings using the Joint Inter-Sectoral Analysis Framework methodology.
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/4f743624-c0d3-4449-b032-86ae79dff1b9/download/iraq_hno_2020_pin_acutepin_severity_20211111.xlsx
  format: null
  id: resource_4f743624
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRAQ_HNO_2020_PIN_AcutePIN_Severity_20211111.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (Iraq Humanitarian Needs Overview
    2020)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/1b77da7d-d847-4ba8-972c-817d07680df0/download/irq_hno_2020.xlsx
  format: null
  id: resource_1b77da7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRQ_HNO_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (Iraq Humanitarian Needs Overview
    2019)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/efa27213-f5b6-4fba-be19-73c89c7f32fd/download/pin_hno_2019_irq_hdx.xlsx
  format: null
  id: resource_efa27213
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRQ_HNO_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Humanitarian Needs Overview (Iraq Humanitarian Needs Overview
    2015 - 2016)
  download_url: https://data.humdata.org/dataset/1095c875-00e2-44ce-911f-7e9e285ecfc5/resource/e0705ed4-4a24-40a9-90ce-f2c7d0b8078a/download/20160105_iraq-humanitarian-needs-overview.xlsx
  format: null
  id: resource_e0705ed4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRQ_HNO_2015-2016.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_ochairq_humanitarianneedsoverview_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: Iraq - Humanitarian Needs Overview
version: null
vulnerability: null
---
