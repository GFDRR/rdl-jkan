---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/syrian-arab-republic-displacement-data-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/syrian-arab-republic-displacement-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/syrian-arab-republic-displacement-data-iom-dtm
dataset_id: rdls_lss-syr_iom_arabrepublicdisplacementd_2025
description: 'The Displacement Tracking Matrix (DTM) is a suite of methodological
  tools designed to track and monitor mobility. Leveraging its formal Humanitarian
  Needs Assessment Programme (HNAP) experience, DTM Syria was activated on 1 February
  2025 to collect primary data. Following the rapid power shift in Damascus on 8 December
  2024, Syria is undergoing a pivotal transformation, reshaping its humanitarian,
  political, and recovery landscape. This change has intensified population movements,
  exacerbating the complexities of displacement and return patterns.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/syrian-arab-republic-displacement-data-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: DTM Syria collected primary data on population movements through baseline
    assessments conducted monthly from February to October 2025, following the rapid
    political transformation in December 2024. Data was aggregated at multiple administrative
    levels (governorate, district, sub-district, location) with spatial coordinates,
    tracking displacement flows, returns, and new arrivals as post-event impact records.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/syrian-arab-republic-displacement-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees tracked following the
      December 2024 power shift in Syria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: New residents and arrivals from abroad tracked as population movements
      post-December 2024
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, the
    Syrian Arab Republic (hereinafter referred to as Syria) is undergoing a pivotal
    transformation, reshaping its humanitarian, political, demographic, and recovery
    landscape. As a sub-component of mobility tracking, the baseline assessment provides
    critical data on Internally Displaced Persons (IDPs), returnees within Syria,
    and arrivals from abroad, whether to their place of origin or a different location.
    Across Syria's 14 governorates, the population landscape is shaped by significant
    mobility patterns. This assessment provides a comprehensive overview of DTM's
    mobility trends among IDPs, IDP returnees and arrivals from abroad during October
    2025, as well as updated baseline figures, offering insights to support humanitarian
    response and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/e3c2994c-324e-41dd-a646-c82e211c4ba0/download/oct-baseline-2025-final_hdx.xlsx
  format: null
  id: resource_e3c2994c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 9 - October 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, the
    Syrian Arab Republic (hereinafter referred to as Syria) is undergoing a pivotal
    transformation, reshaping its humanitarian, political, demographic, and recovery
    landscape. As a sub-component of mobility tracking, the baseline assessment provides
    critical data on Internally Displaced Persons (IDPs), returnees within Syria,
    and arrivals from abroad, whether to their place of origin or a different location.
    Across Syria's 14 governorates, the population landscape is shaped by significant
    mobility patterns. This assessment provides a comprehensive overview of DTM's
    mobility trends among IDPs, IDP returnees and arrivals from abroad during August
    2025, as well as updated baseline figures, offering insights to support humanitarian
    response, and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/529bf769-4e1b-43e0-9e3e-b07139dcd5e4/download/mmt-dataset-august-2025-round-7_hdx.xlsx
  format: null
  id: resource_529bf769
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 7 - August 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, the
    Syrian Arab Republic (hereinafter referred to as Syria) is undergoing a pivotal
    transformation, reshaping its humanitarian, political, demographic, and recovery
    landscape. As a sub-component of mobility tracking, the baseline assessment provides
    critical data on Internally Displaced Persons (IDPs), returnees within Syria,
    and arrivals from abroad, whether to their place of origin or a different location.
    Across Syria's 14 governorates, the population landscape is shaped by significant
    mobility patterns. This assessment provides a comprehensive overview of DTM's
    mobility trends among IDPs, IDP returnees and arrivals from abroad during July
    2025, as well as updated baseline figures, offering insights to support humanitarian
    response, and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/fc2ae6e1-7f4a-4336-b787-440800c2bb24/download/mmt-dataset-july-2025-round-6_hdx.xlsx
  format: null
  id: resource_fc2ae6e1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 6 - July 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, the
    Syrian Arab Republic (henceforth referred to as Syria) is undergoing a pivotal
    transformation, reshaping its humanitarian, political, demographic, and recovery
    landscape. As a sub-component of mobility tracking, the baseline assessment provides
    critical data on Internally Displaced Persons (IDPs), returnees within Syria,
    and arrivals from abroad, whether to their place of origin or a different location.
    Across Syria's 14 governorates, the population landscape is shaped by significant
    mobility patterns. This assessment provides a comprehensive overview of mobility
    trends among IDPs, IDP returnees and arrivals from abroad during June 2025, as
    well as updated baseline figures, offering insights to support humanitarian response,
    and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/44ba5d44-75fd-42a6-b375-f2f7aef3dc08/download/03.-dataset-mmt-june-2025-3_final_hdx.xlsx
  format: null
  id: resource_44ba5d44
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 5 - Jun 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, the
    Syrian Arab Republic (henceforth referred to as Syria) is undergoing a pivotal
    transformation, reshaping its humanitarian, political, demographic, and recovery
    landscape. As a sub-component of mobility tracking, the baseline assessment provides
    critical data on Internally Displaced Persons (IDPs), returnees within Syria,
    and arrivals from abroad, whether to their place of origin or a different location.
    Across Syria's 14 governorates, the population landscape is shaped by significant
    mobility patterns. This assessment provides a comprehensive overview of mobility
    trends among IDPs, IDP returnees and arrivals from abroad during May 2025, as
    well as updated baseline figures, offering insights to support humanitarian response,
    and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/bd7d7cc8-e77e-45c0-b1c4-bec5ccaef565/download/syrian-arab-republic-population-mobility-and-baseline-assessment-round-4-v2_hdx.xlsx
  format: null
  id: resource_bd7d7cc8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 4 - May 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, Syria
    is undergoing a pivotal transformation, reshaping its humanitarian, political,
    and recovery landscape. As a sub-component of mobility tracking, the baseline
    assessment provides critical data on Internally Displaced Persons (IDPs), returnees
    within Syria, and arrivals from abroad, whether to their place of origin or a
    different location. Across Syria's 14 governorates, the population landscape is
    shaped by significant mobility patterns. The country is made up of 26.3 million
    residents, including 6.5 million internally displaced persons (IDPs), 1.3 million
    IDP returnees, and 729,971 arrivals from abroad. This assessment provides a comprehensive
    overview of mobility trends among IDPs, IDP returnees and arrivals from abroad
    during April 2025, as well as updated baseline figures, offering insights to support
    humanitarian response, and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/153f3d40-6f09-441b-a13e-b89bdc1aa168/download/syrian-arab-republic-population-mobility-and-baseline-assessment-round-3-apr-2025_hdx.xlsx
  format: null
  id: resource_153f3d40
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 3 - Apr 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Following the rapid power shift in Damascus on 8 December 2024, Syria
    is undergoing a pivotal transformation, reshaping its humanitarian, political,
    and recovery landscape. As a sub-component of mobility tracking, the baseline
    assessment provides critical data on Internally Displaced Persons (IDPs), returnees
    within Syria, and arrivals from abroad, whether to their place of origin or a
    different location. With a demographic composition of 17.7 million residents,
    6.7 million IDPs, 1.2 million IDP returnees, and nearly 700,000 arrivals from
    abroad across Syria's 14 governorates, mobility patterns continue to significantly
    shape the country's population landscape This assessment provides a comprehensive
    overview of mobility trends among IDPs, returnees and arrivals from abroad during
    March 2025, as well as updated baseline figures, offering insights to support
    humanitarian response, and long-term reintegration efforts in Syria.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/875a2e7a-2a4c-468a-bd91-33d03722b964/download/syrian-arab-republic-population-mobility-and-baseline-assessment-round-2_hdx.xlsx
  format: null
  id: resource_875a2e7a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 2 - March 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: After 1 November 2024, there were 178,788 new IDPs within Syria. Since
    2011, the total number of IDPs within Syria stands at 6,994,646, with the majority
    (4.88 million) residing in residential areas and 2.11 million in camp settings.
    Most displacement movements occurred in November and December 2024, driven by
    intensified military operations. However, a notable decline in displacement has
    been observed since mid-December, indicating a relative stabilization in movement
    patterns. IDPs located in camp settings are predominantly from Idleb, Aleppo,
    and Hama; while IDPs in non-camp settings are from Rural Damascus and Aleppo.
    As of 1 November 2024, 723,380 individuals have returned within Syria, resulting
    in a total of 1,075,807 IDP returnees since January 2024. Notably, the trend of
    return intensified in January 2025, likely driven by both the stabilization of
    the country and the new authorities' promises of an inclusive government, recovery,
    and a clear path forward for Syria. Lattakia and Aleppo are governorates from
    where a large majority of IDPs returned.
  download_url: https://data.humdata.org/dataset/cec958be-72a7-4ef3-a98b-84dfbbf6639c/resource/19dafb97-d99b-4cc1-b45d-811c1ae3ca77/download/dtm-syria-baseline-assessment-round-1-feb-25.xlsx
  format: null
  id: resource_19dafb97
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syrian Arab Republic - Baseline Assessment - Round 1 - Feb 2025
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_iom_arabrepublicdisplacementd_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-30'
  start: '2025-02-01'
temporal_resolution: null
title: Syrian Arab Republic Displacement Data [IOM DTM]
version: null
vulnerability: null
---
