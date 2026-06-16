---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/asm-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/asm-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/asm-anomalies-fapar-viirs
dataset_id: rdls_hzd-asm_copernicus_americansamoavegetationin_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/asm-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FAPAR:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values derived from VIIRS satellite observations are processed
    into 10-day temporal composites. Anomalies are calculated at each grid cell as
    the deviation from a long-term mean baseline (2012 to last complete year), enabling
    detection and monitoring of agricultural drought impacts on vegetation growth
    and productivity across American Samoa.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/asm-anomalies-fapar-viirs
  rel: source
loss:
  losses: []
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
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_fapar_viirs.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/50e50fda-0126-4112-a23b-bdafe284254a/download/asm_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_50e50fda
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/66567363-ef01-4d75-9d19-0b16a2c811dc/download/asm_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_66567363
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/9031608f-3efd-440a-b453-b9bef04b103b/download/asm_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_9031608f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/ad0aea45-875a-44d5-87f3-000064665d09/download/asm_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_ad0aea45
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/2929dcd8-1777-4fe9-aec5-84851ddcc620/download/asm_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_2929dcd8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/de616be0-607e-44e5-ac34-65b9b7cc7cc7/download/asm_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_de616be0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/1e87594a-a30a-4515-8b72-c96da6a0fe05/download/asm_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_1e87594a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/86131b26-e29e-4b2c-8765-9d11e1c6b8a5/download/asm_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_86131b26
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/3483c966-e096-4eb3-af34-8f3d5339e5d0/download/asm_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_3483c966
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/974c936c-d24a-4a56-a7ac-723ace6c3f6e/download/asm_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_974c936c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/c432503c-5f0d-489e-80c1-9abab8fc949f/download/asm_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_c432503c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/53fd25a9-12b8-4175-be58-9e535941974c/download/asm_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_53fd25a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/ca3d0b6d-b6f9-43c2-8500-d658016efb5c/download/asm_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_ca3d0b6d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/a3fc02cc-261a-4052-841c-e0c94d899b7e/download/asm_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_a3fc02cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/ed5fcd55-6a27-4f9c-b3bd-31e4813c0b3c/resource/45abbce2-f7ba-4b4d-82bc-e3799da3e25b/download/asm_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_45abbce2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-asm_copernicus_americansamoavegetationin_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - ASM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'American Samoa: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
