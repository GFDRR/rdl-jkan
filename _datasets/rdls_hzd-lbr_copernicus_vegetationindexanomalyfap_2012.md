---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/lbr-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/lbr-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/lbr-anomalies-fapar-viirs
dataset_id: rdls_hzd-lbr_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/lbr-anomalies-fapar-viirs]'
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
      calculation_method: observed
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
  description: FAPAR values from VIIRS satellite observations are collected in 10-day
    time composites. Anomalies are calculated at each grid cell as the deviation from
    a long-term mean baseline (2012 to the last available full year), enabling detection
    and monitoring of agricultural drought impacts on vegetation growth and productivity
    across Liberia.
  sources:
  - id: source_1
    license: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lbr-anomalies-fapar-viirs
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
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/49cf945d-ed84-47b5-84db-73ccc72614dd/download/lbr_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_49cf945d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/2d416518-4f7f-4f31-85c4-2bd7f4a13806/download/lbr_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_2d416518
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/d8d0c09e-3e33-4d60-90c2-29ab9ef4151b/download/lbr_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_d8d0c09e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/d7e7dbd0-e0bb-4b1d-9393-0b1b85af29ee/download/lbr_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_d7e7dbd0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/6ffdb302-f31e-4803-ba14-d00b90b7ceab/download/lbr_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_6ffdb302
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/f52ed349-4fb9-42d3-81cc-7e3f0834737f/download/lbr_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_f52ed349
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/b6232aca-e31b-4186-9bae-34147691bf6f/download/lbr_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_b6232aca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/64b70de3-f42a-459f-b3f4-d983abc8a155/download/lbr_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_64b70de3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/9b7d3468-a32d-4a79-859d-2136c7c09bab/download/lbr_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_9b7d3468
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/98d63057-b65d-470c-9c99-6e729de6c0c9/download/lbr_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_98d63057
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/c034424d-3aa8-429f-bdf7-b35f2d2cca0d/download/lbr_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_c034424d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/b1235ac6-9dac-44f6-8a3e-7f3275aa8606/download/lbr_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_b1235ac6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/66299736-fa04-4aec-8a20-3172d541578e/download/lbr_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_66299736
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/c183ce32-45ab-4f22-ba93-1fefa232bf74/download/lbr_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_c183ce32
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/4d2bffaa-1f4d-4280-9e3e-34acec8b8ef9/resource/3c48c712-b21c-4f04-b26a-c194cb63d24a/download/lbr_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_3c48c712
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lbr_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - LBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Liberia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
