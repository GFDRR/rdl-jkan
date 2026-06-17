---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/brb-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/brb-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/brb-anomalies-fapar-viirs
dataset_id: rdls_hzd-brb_copernicus_barbadosvegetationindexan_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/brb-anomalies-fapar-viirs]'
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
  type: drought
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals and processed into anomalies by calculating the deviation from a long-term
    mean baseline (2012 to the last available full year) at each grid cell. The resulting
    raster datasets are distributed as annual GeoTIFF files to enable monitoring of
    agricultural drought impacts on vegetation productivity.
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
- href: https://data.humdata.org/dataset/brb-anomalies-fapar-viirs
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
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/c237b985-ac41-4d19-a512-cabeeef5498e/download/brb_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_c237b985
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/109bb849-e014-4312-be92-fd1143517320/download/brb_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_109bb849
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/3603cb11-6ddb-4f80-8d75-65eece98c1c3/download/brb_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_3603cb11
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/0891c07a-d6c6-4be0-9d58-787850aeda24/download/brb_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_0891c07a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/ac399492-4d72-41a7-ba41-12e50a939801/download/brb_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_ac399492
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/9a718a2f-011f-41ef-9946-7638f38f7e72/download/brb_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_9a718a2f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/22df5c2c-a0ec-4c53-9451-05349695c278/download/brb_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_22df5c2c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/0dfbb1a5-1f0a-4a31-ac4e-80eedbe35b57/download/brb_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_0dfbb1a5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/0729911c-8fde-4e98-ba30-20499ed8e74f/download/brb_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_0729911c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/5b536eee-0e7a-4bae-9ede-df368154d8bf/download/brb_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_5b536eee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/fbff8cae-58fa-4a5b-8c92-3dcd1f7a8ccb/download/brb_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_fbff8cae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/9b27cfc3-34d6-4d83-95d1-46b2b62c3a1c/download/brb_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_9b27cfc3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/04f30a38-76bf-42c1-b49e-e818916e493d/download/brb_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_04f30a38
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/b3e8316a-6bcd-4de0-aaca-a542ea0483c3/download/brb_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_b3e8316a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/6c1a0d85-af2d-4f68-bd8e-173b3bb9d99c/resource/fa56f963-0cb3-4c89-9dc7-940640711554/download/brb_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_fa56f963
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brb_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-brb_copernicus_barbadosvegetationindexan_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - BRB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Barbados: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
