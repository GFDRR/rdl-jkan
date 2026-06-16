---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
creator:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
dataset_id: rdls_hzd-tza_resilienceacade_meteorprojectseismichazar
description: "Seismic Hazard Map showing mean Peak Ground Acceleration (PGA) in g\
  \ for a 10% probability of exceedence in 50 years for the country of Tanzania. This\
  \ layer was uploaded as part of the METEOR Project, please see http://meteor-project.org/\
  \ for details. If you find this data useful, please please provide feedback via\
  \ our questionnaire, it should take only a few minutes: https://forms.gle/DQjhE89CRegNKB3X8\
  \ This map was produced using the GEM OpenQuake engine using the SSAHARA model produced,\
  \ please see https://hazard.openquake.org/gem/models/SSA/ for further details. Cite\
  \ this work as: Poggi, V., Durrheim, R., Mavonga Tuluka, G., Weatherill, G., Gee,\
  \ R., Pagani, M., Nyblade, A., Delvaux, D., 2017. Assessing Seismic Hazard of the\
  \ East African Rift: a pilot study from GEM and AfricaArray. Bulletin of Earthquake\
  \ Engineering. Volume 15, Issue 11, 4499-4529, DOI: 10.1007/s10518-017-0152-4 \xC2\
  \xA9 2021 GEM Foundation and the METEOR Project Consortium.. [Source: This metadata\
  \ record was automatically extracted from the GeoNode portal resilienceacademy]"
details: OGC:CRS84 - WGS 84 (CRS84) - Geographic.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Data collected and curated through the Resilience Academy community
    mapping programme. Quality reviewed during the data curation process.
  sources:
  - id: source_1
    license: null
    name: Monica Timbuka
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/701
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Theofrida Maginga
  url: https://geonode.resilienceacademy.ac.tz
purpose: Risk awareness and risk mitigation..
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (Prj)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/101/link
  format: Prj
  id: resource_0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: output_19017_hazard_map_mean_24306de437f136381
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:output_19017_hazard_map_mean_24306de437f136381
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'METEOR Project Seismic Hazard Map for Tanzania (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:output_19017_hazard_map_mean_24306de437f136381&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:output_19017_hazard_map_mean_24306de437f136381
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'METEOR Project Seismic Hazard Map for Tanzania (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:output_19017_hazard_map_mean_24306de437f136381&outputFormat=application%2Fjson
  format: null
  id: resource_2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_6
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_7
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Seismic Hazard Map for Tanzania (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aoutput_19017_hazard_map_mean_24306de437f136381&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tza_resilienceacade_meteorprojectseismichazar
spatial:
  bbox:
  - 29.34517
  - -11.72812
  - 40.43317
  - -1.00012
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2019
  duration: null
  end: null
  start: null
temporal_resolution: null
title: METEOR Project Seismic Hazard Map for Tanzania
version: '2019'
vulnerability: null
---
