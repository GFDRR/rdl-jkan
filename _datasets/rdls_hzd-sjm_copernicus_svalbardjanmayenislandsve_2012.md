---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/sjm-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/sjm-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/sjm-anomalies-fapar-viirs
dataset_id: rdls_hzd-sjm_copernicus_svalbardjanmayenislandsve_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/sjm-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values are derived from VIIRS satellite observations in 10-day
    composites. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline spanning 2012 to the most recent complete year. The resulting
    raster datasets enable temporal monitoring of vegetation health deviations to
    detect and assess agricultural drought impacts.
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
- href: https://data.humdata.org/dataset/sjm-anomalies-fapar-viirs
  rel: source
loss: null
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
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/b435ca7e-37ce-4a13-90e6-8ff63437144c/download/sjm_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_b435ca7e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/c23217b9-3dd8-4ec8-b0b9-7fecd40ca5d7/download/sjm_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_c23217b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/96605731-676e-430e-bcc0-360833de7dc1/download/sjm_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_96605731
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/135063b6-25c7-4db6-8595-139771944d43/download/sjm_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_135063b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/e7a24af6-3bfd-4130-8811-5ad890c69ee8/download/sjm_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_e7a24af6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/ae40c0f1-60a0-40b1-b90b-7dba8a3f5b38/download/sjm_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_ae40c0f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/b5da26e6-a066-42dd-9069-98b2aa44c067/download/sjm_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_b5da26e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/977ca213-7d0a-4f92-a4b9-156cb0fb9520/download/sjm_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_977ca213
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/f54c8dee-e645-48b1-a852-7b73b469d133/download/sjm_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_f54c8dee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/fc8170a3-e67c-4c16-8c81-d705a7132712/download/sjm_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_fc8170a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/602bec0b-adc1-4a79-b88a-7f12aa6b427d/download/sjm_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_602bec0b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/c5988eae-4f1b-4c98-87ed-0d75342155ac/download/sjm_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_c5988eae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/83106028-e1af-47da-8bdd-ea9faae483e9/download/sjm_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_83106028
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/1de00bf6-b048-4404-95a1-0dd16a42c23f/download/sjm_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_1de00bf6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/90c420a7-8b4e-4aa0-9885-d25153f8e7a7/resource/b08ca154-572a-4327-8a35-bdb002e56c43/download/sjm_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_b08ca154
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sjm_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sjm_copernicus_svalbardjanmayenislandsve_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - SJM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Svalbard and Jan Mayen Islands: Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
