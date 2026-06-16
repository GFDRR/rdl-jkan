---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/mali-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team and partners
    url: https://data.humdata.org/dataset/mali-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/mali-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/mali-humanitarian-needs
dataset_id: rdls_lss-mli_ochahpc_needs_2017
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mali-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Humanitarian needs data compiled by UNOCHA from cluster-based assessments
    across Mali's regions and administrative divisions. People in need estimates are
    derived by summing the highest figures proposed by each cluster per region, disaggregated
    by age and gender. The dataset consolidates multi-year humanitarian situation
    reports (2017-2026) to support joint strategic response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian Country Team and partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mali-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by humanitarian crisis in Mali, estimated through
      cluster-based needs assessments
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (PDI) in Mali requiring humanitarian
      assistance
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/attachments/5e85c4c4-ab23-4469-849e-bf95f3c7d1a2/HPC_2023-HNO_VF.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/7dc50bcd-44fc-44e8-be72-4b9a6edaaf13/download/mli_hpc_needs_api_2026.csv
  format: null
  id: resource_7dc50bcd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/b43f3634-d721-4884-a4b5-8862ebab3547/download/mli_hpc_needs_api_2025.csv
  format: null
  id: resource_b43f3634
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/7dd03816-0627-4168-8dba-744007aa4612/download/mli_hpc_needs_api_2024.csv
  format: null
  id: resource_7dd03816
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2024 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/1a3206f3-2ac6-49e0-a70c-04206f651e92/download/mali_hno_2024.4.xlsx
  format: null
  id: resource_1a3206f3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2023 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/ad101ccd-90cc-4f5f-896d-1f808f04e99e/download/mali-hpc-2023_hdx1.xlsx
  format: null
  id: resource_ad101ccd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2022 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/bc973e6f-b455-4fb5-a146-30573e2dc8dc/download/mli_chiffres-desagreges-hpc-2022-1.xlsx
  format: null
  id: resource_bc973e6f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2021 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/73f9a436-605c-4d95-81ee-339d75808e92/download/mli_hno_2021-vf.xlsx
  format: null
  id: resource_73f9a436
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2020 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/652aa614-e640-41b2-a3dd-ccec839bee20/download/mli_hno_2020.xlsx
  format: null
  id: resource_652aa614
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2019 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/c5ab224e-1eed-46f0-9a81-e03daf550f28/download/mli_hno_2019.xlsx
  format: null
  id: resource_c5ab224e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2018 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/d9e809cd-c5dd-4bac-9cc7-fda9bf76ae09/download/mli_hno_2018.xlsx
  format: null
  id: resource_d9e809cd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Mali Humanitarian Needs 2017 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/8bdcfd59-0541-4846-848f-56750e2e03f5/resource/cc0af470-63e6-4735-80f0-e6e4863604fb/download/ml_hno_2017.xlsx
  format: null
  id: resource_cc0af470
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli_hpc_needs_2017
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochahpc_needs_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Mali: Humanitarian Needs'
version: null
vulnerability: null
---
