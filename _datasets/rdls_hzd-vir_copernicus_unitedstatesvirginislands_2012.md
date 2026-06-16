---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/vir-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/vir-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/vir-anomalies-fapar-viirs
dataset_id: rdls_hzd-vir_copernicus_unitedstatesvirginislands_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/vir-anomalies-fapar-viirs]'
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
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are processed into 10-day
    temporal composites. FAPAR anomalies are calculated at each grid cell as the deviation
    from a long-term mean baseline (2012 to the last available full year), generating
    raster datasets to monitor agricultural drought impacts on vegetation greenness
    and productivity.
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
- href: https://data.humdata.org/dataset/vir-anomalies-fapar-viirs
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
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/b6f4da3e-914d-4d29-8c0c-eaca63079f2d/download/vir_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_b6f4da3e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/d7998b8a-cf07-46c6-9064-24ad4b2760c9/download/vir_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_d7998b8a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/b11f7b4f-f3ed-4883-9a94-5f500a68e0c4/download/vir_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b11f7b4f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/c4b939af-3a3c-4225-93ae-b9f59b9e9c96/download/vir_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_c4b939af
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/c21e8247-87af-4f57-b164-7d66876df84b/download/vir_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_c21e8247
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/3493273f-4b1f-4243-9035-b557fc99989a/download/vir_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_3493273f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/d9e6bb75-fd8b-4df6-bebd-7346e2a50ef1/download/vir_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_d9e6bb75
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/7a2bbe45-ab99-4795-8e81-258d4af877d3/download/vir_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_7a2bbe45
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/8663e296-cd6f-41ef-b442-60fde946bc0d/download/vir_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_8663e296
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/3fc9a4cc-7dcf-4fb6-bd35-e0ceb5fccda7/download/vir_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_3fc9a4cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/ff4e30d3-c890-4871-bea6-b1cfd3ce380f/download/vir_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_ff4e30d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/6afd2bac-f836-4c08-9470-789f1b04ed18/download/vir_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_6afd2bac
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/50d4c8dc-5835-49ea-af12-5525e53daf27/download/vir_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_50d4c8dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/0ac93ed4-9752-4195-af95-cb9752963cad/download/vir_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_0ac93ed4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/a6774531-cc87-489e-84b8-7e1f3894ed05/resource/d85690b6-172e-4164-8b9e-8c884a2d6087/download/vir_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_d85690b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vir_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vir_copernicus_unitedstatesvirginislands_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - VIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'United States Virgin Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
