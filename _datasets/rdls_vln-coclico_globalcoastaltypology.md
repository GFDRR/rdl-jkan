---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
dataset_id: rdls_vln-coclico_globalcoastaltypology
description: 'This dataset provides a globally consistent, high-resolution (100 m)
  coastal typology, derived from satellite imagery and elevation data using a deep
  learning model. It provides a foundational dataset for coastal-change analysis,
  erosion assessment, and more broader coastal vulnerability mapping and coastal adaptation
  in the face of accelerating climate change. Using a supervised multi-task convolutional
  neural network, we classified four coastal attributes along the cross-shore profile
  for nearly 10 million transects from the Global Coastal Transect System (GCTS):
  1. Sediment Type: e.g., sandy, gravel or shingle; muddy; rocky; or, no sediment.
  2. Coastal Type: e.g., cliffed or steep, sediment plain, wetlands, or dune systems.
  3. Built Environment: Presence or absence of human development. 4. Coastal Defenses:
  Presence or absence of human-made coastal defenses. The model achieves strong predictive
  performance (F1 scores: 0.67-0.83). Results show that ~61% of the global coastline
  consists of soft, potentially erodible sediments. Among sandy, gravel, or shingle
  coasts, 20% are cliff-backed and 16.5% are located on built-up coasts. Data are
  stored in a cloud-optimized, partitioned Parquet format. Tutorials and usage examples
  are available via the coastpy Python library: https://github.com/TUDelft-CITG/coastpy.
  Please cite the associated publication when using this dataset: Calkoen et al.,
  2025, *Mapping the world''s coast: a global 100 m coastal typology derived from
  satellite data using deep learning*, Earth System Science Data (in review at https://essd.copernicus.org/preprints/essd-2025-388/).
  DOI paper: https://doi.org/10.5194/essd-2025-388 DOI dataset: https://doi.org/10.5281/zenodo.15599096.
  [Source: This metadata record was automatically extracted from the STAC catalog
  coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: 'This dataset provides a globally consistent, high-resolution (100
    m) coastal typology, derived from satellite imagery and elevation data using a
    deep learning model. It provides a foundational dataset for coastal-change analysis,
    erosion assessment, and more broader coastal vulnerability mapping and coastal
    adaptation in the face of accelerating climate change. Using a supervised multi-task
    convolutional neural network, we classified four coastal attributes along the
    cross-shore profile for nearly 10 million transects from the Global Coastal Transect
    System (GCTS): 1. Sediment Type: e.g., sandy, gravel or shingle; muddy; rocky;
    or, no sediment. 2. Coastal Type: e.g., cliffed or steep, sediment plain, wetlands,
    or dune systems. 3. Built Environment: Presence or absence of human development.
    4. Coastal Defenses: Presence or absence of human-made coastal defenses. The model
    achieves strong predictive performance (F1 scores: 0.67-0.83). Results show that
    ~61% of the global coastline consists of soft, potentially erodible sediments.
    Among sandy, gravel, or shingle coasts, 20% are cliff-backed and 16.5% are located
    on built-up coasts. Data are stored in a cloud-optimized, partitioned Parquet
    format. Tutorials and usage examples are available via the coastpy Python library:
    https://github.com/TUDelft-CITG/coastpy. Please cite the associated publication
    when using this dataset: Calkoen et al., 2025, *Mapping the world''s coast: a
    global 100 m coastal typology derived from satellite data using deep learning*,
    Earth System Science Data (in review at https://essd.copernicus.org/preprints/essd-2025-388/).
    DOI paper: https://doi.org/10.5194/essd-2025-388 DOI dataset: https://doi.org/10.5281/zenodo.15599096'
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://deltares.nl
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: 'Calkoen, F. R., Luijendijk, A. P., Hanson, S., Nicholls, R. J., Moreno-Rodenas,
    A., De Heer, H., and Baart, F.: Mapping the world''s coast: a global 100-m coastal
    typology derived from satellite data using deep learning, Earth Syst. Sci. Data
    Discuss. [preprint], https://doi.org/10.5194/essd-2025-388, in review, 2025.'
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/global-coastal-typology/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/global-coastal-typology/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Global Coastal Typology [global-coastal-typology]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global Coastal Typology (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
  download_url: https://coclico.blob.core.windows.net/items/global-coastal-typology.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-coclico_globalcoastaltypology
spatial:
  bbox:
  - -179.99979945991507
  - -78.74747176732404
  - 179.9998718338963
  - 83.66967471602302
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025'
  start: '2025'
temporal_resolution: null
title: CoCliCo - Global Coastal Typology
version: null
vulnerability: null
---
