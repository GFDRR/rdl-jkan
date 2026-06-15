---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/gtm-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gtm-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gtm-anomalies-fapar-viirs
dataset_id: rdls_hzd-gtm_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gtm-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline (2012 to last available full year), enabling detection
    and monitoring of agricultural drought impacts on vegetation growth and productivity
    across Guatemala.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gtm-anomalies-fapar-viirs
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
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/54fc0a47-1228-4ad1-b394-6c2813804bc7/download/gtm_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_54fc0a47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/6e24cc2d-c164-4438-828d-51906638a0ff/download/gtm_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_6e24cc2d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/c6ac103d-0bd3-4e69-88bb-e8be3a815583/download/gtm_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_c6ac103d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/889dd498-1e3d-4109-80ce-38f435be53a3/download/gtm_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_889dd498
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/b6261044-8651-447e-b580-e5df1144e4fc/download/gtm_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_b6261044
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/3606d66c-61db-4ce6-84ef-ef4d6981478c/download/gtm_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_3606d66c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/32949d5e-949d-4906-9e89-7654566a66d5/download/gtm_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_32949d5e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/ae5b9eb3-5ce9-4fe9-9609-3090948ff080/download/gtm_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_ae5b9eb3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/7bb8a33f-7d1d-462f-8656-84eb7d72821c/download/gtm_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_7bb8a33f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/1732c7bf-50e9-4fad-9072-27f5722eb00e/download/gtm_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_1732c7bf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/525b11c5-5d14-4ea1-8109-fec533b4e8be/download/gtm_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_525b11c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/86aa6870-383c-4a5e-8d43-e2c3fc8ba517/download/gtm_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_86aa6870
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/70f4bfd3-2624-4544-acec-976558ba6bc2/download/gtm_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_70f4bfd3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/d1f97575-12c8-4703-bccf-8baacfa97f15/download/gtm_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_d1f97575
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/6024fcb5-cd1b-4f27-b7ef-14e82bc5c3b5/resource/72669f32-6108-4c08-94e1-cff7956b1f68/download/gtm_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_72669f32
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gtm_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gtm_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Guatemala: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
